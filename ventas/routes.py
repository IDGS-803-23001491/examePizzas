from . import ventas
from flask import request, render_template,redirect, url_for, flash
from models import db, DetalleTemporal, Clientes,  Pedidos, Pizzas, DetallePedido
from datetime import date
from sqlalchemy import func

import forms

@ventas.route("/ventas",methods=["GET","POST"])
def index():
	pedido_form = forms.PedidoForm(request.form)
	pizza_form = forms.PizzaForm(request.form)
	detalles = DetalleTemporal.query.all()
	hoy = date.today()
	pedidos = Pedidos.query.filter_by(fecha=hoy).all()
	total_hoy = db.session.query(func.sum(Pedidos.precio)).filter(
    	Pedidos.fecha == hoy).scalar() or 0

	if request.method == "POST":
		accion = request.form.get("accion")

		if accion == "agregar" and pizza_form.validate() and pedido_form.validate():
			ingredientes = sorted(pizza_form.ingredientes.data)
			lista_i = ",".join(ingredientes)
			pizza = DetalleTemporal.query.filter_by(
					tamano=pizza_form.tamano.data,
					ingredientes=lista_i
				).first()
			
			if pizza:
				pizza.cantidad = pizza.cantidad + pizza_form.cantidad.data
				pizza.subtotal = pizza.precio * pizza.cantidad
				db.session.add(pizza)
			else:
				subtotal = 0
				tamano = pizza_form.tamano.data
				ingredientes = sorted(pizza_form.ingredientes.data)
				lista_i = ",".join(ingredientes)
				cantidad_i = len(ingredientes)
				cantidad_p = pizza_form.cantidad.data

				if tamano == "Chica":
					subtotal = (40 + (cantidad_i * 10)) * cantidad_p
				if tamano == "Mediana":
					subtotal = (80 + (cantidad_i * 10)) * cantidad_p
				if tamano == "Grande":
					subtotal = (120 + (cantidad_i * 10)) * cantidad_p

				dt = DetalleTemporal(
				tamano = tamano,
				ingredientes = lista_i,
				precio = subtotal / cantidad_p,
				cantidad = cantidad_p,
				subtotal = subtotal
				)
				db.session.add(dt)
				
			db.session.commit()
			flash("Pizza agregada correctamente", "success")
		elif accion == "terminar" and pedido_form.validate():

			c = Clientes(
				nombre = pedido_form.nombre.data,
				direccion = pedido_form.direccion.data,
				telefono = pedido_form.telefono.data
			)

			db.session.add(c)
			db.session.commit()

			detalles = DetalleTemporal.query.all()
			total_p = db.session.query(func.sum(DetalleTemporal.precio)).scalar() or 0

			p = Pedidos(
				id_cliente = Clientes.query.count(),
				fecha = pedido_form.fecha.data,
				precio = total_p
			)

			db.session.add(p)
			db.session.commit()

			for d in detalles:
				pizza = Pizzas.query.filter_by(
					tamano=d.tamano,
					ingredientes=d.ingredientes
				).first()

				if pizza:
					dp = DetallePedido(
						id_pedido = Pedidos.query.count(),
						id_pizza = pizza.id_pizza,
						cantidad = d.cantidad,
						subtotal = d.subtotal
					)

					db.session.add(dp)
					db.session.commit()
				else:
					pz = Pizzas(
						tamano = d.tamano,
						ingredientes = d.ingredientes,
						precio = d.precio
					)

					db.session.add(pz)
					db.session.commit()

					dp = DetallePedido(
						id_pedido = Pedidos.query.count(),
						id_pizza = Pizzas.query.count(),
						cantidad = d.cantidad,
						subtotal = d.subtotal
					)

					db.session.add(dp)
					db.session.commit()
			
			DetalleTemporal.query.delete()
			db.session.commit()

			flash("Pedido realizado correctamente", "success")

			return redirect(url_for('ventas.index'))
		elif accion.isnumeric():
			dt = db.session.query(DetalleTemporal).filter(DetalleTemporal.id_detalle == int(accion)).first()
			db.session.delete(dt)
			db.session.commit()
			flash("Pizza eliminada correctamente", "success")
		else:
			flash("Porfavor introduzca los datos necesarios", "error")

		pizza_form = forms.PizzaForm()
		detalles = DetalleTemporal.query.all()

	return render_template("ventas/index.html",pedido=pedido_form,pizza=pizza_form,
						detalles = detalles, pedidos = pedidos, total = total_hoy)

@ventas.route("/ventas/dia",methods=["GET","POST"])
def venta_dia():
	
	form = forms.ConsultaForm(request.form)
	dia = date.today().weekday()

	pedidos = Pedidos.query.filter(
		func.weekday(Pedidos.fecha) == dia
	).all()
	
	if request.method == "POST":
		dia = form.dia.data
		pedidos = Pedidos.query.filter(
			func.weekday(Pedidos.fecha) == dia
		).all()

	total = db.session.query(func.sum(Pedidos.precio)).filter(
    	func.weekday(Pedidos.fecha) == dia).scalar() or 0
	
	form.dia.data = dia
	return render_template("ventas/listas.html",form=form,pedidos=pedidos, total=total)

@ventas.route("/ventas/mes",methods=["GET","POST"])
def venta_mes():
	
	form = forms.ConsultaForm(request.form)
	mes = date.today().month
	form.dia.data = -1

	pedidos = Pedidos.query.filter(
		func.month(Pedidos.fecha) == mes
	).all()
	
	if request.method == "POST":
		mes = form.mes.data
		pedidos = Pedidos.query.filter(
			func.month(Pedidos.fecha) == mes
		).all()

	total = db.session.query(func.sum(Pedidos.precio)).filter(
    	func.month(Pedidos.fecha) == mes).scalar() or 0
	
	form.mes.data = mes
	return render_template("ventas/listas.html",form=form,pedidos=pedidos, total=total)

@ventas.route("/ventas/detalle")
def detalle():
	id = request.args.get('id')
	pedido = db.session.query(Pedidos).filter(Pedidos.id_pedido == id).first()

	return render_template("ventas/detalle.html",pedido=pedido)
