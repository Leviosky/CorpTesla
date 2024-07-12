from flask import Blueprint, render_template,request,flash, session, redirect, url_for, abort, jsonify
from src.services import check_user_role
from src.services.models import Users, Roles, Client, Services, Proyecto, ProyectoSolar, ClaseDeProyecto, Propuestas, Ventas, Propuestas, Diseño, Revision, Inversor, Inversores, Panel, Bateria
from src.Login import login
from src import db, app
from flask_login import current_user
from werkzeug.utils import secure_filename
from datetime import datetime
import re
import os
import zipfile



home_BP = Blueprint('home_BP', __name__, template_folder='templates',static_folder="static",static_url_path="/src/DashBoard/static/css")
os.makedirs(app.config['UPLOAD_COT'], exist_ok=True)

################# DashBoards Routes ########################
@home_BP.route('/Admin/home')

def AdminDashboard():
    user = current_user
    pagina_actual = 'AdminDashboard'
    return render_template('home_admin.html', pagina_actual=pagina_actual)

@home_BP.route('/Ventas/home')

def VentasDashboard():
    user = current_user
    pagina_actual = 'VentasDashboard'
    return render_template('home_ventas.html', pagina_actual=pagina_actual)

@home_BP.route('/ingeniero/home')

def IngenieroDashboard():
    user = current_user
    pagina_actual = 'IngenieroDashboard'
    return render_template('home_ingeniero.html', pagina_actual=pagina_actual)

@home_BP.route('/Instalador/home')

def InstaladorDashboard():
    user = current_user
    pagina_actual = 'InstaladorDashboard'
    return render_template('home_instalador.html', pagina_actual=pagina_actual)

################################################################


@home_BP.route('/clientes/registro', methods=['GET', 'POST'])
def AddClient():
    pagina_actual = 'AddClient'
    message = ''
    if request.method == 'POST':
        # Obtén los datos del formulario
        ClienteNombre = request.form['nombre']
        ClienteCedula = request.form['cedula']
        ClienteEmail = request.form['correo']
        ClienteTel = request.form['telefono']
        id_services = request.form['servicio']
        ClienteComent = request.form['comentarios']
        ClienteLat = request.form['latitud']
        ClienteLon = request.form['longitud']
        origin_page = request.form.get('origin_page')
        
        messages_to_flash = [] 
        
        
        # Verifica si el cliente ya existe en la base de datos
        cliente_existente_cedula = Client.query.filter_by(ClienteCedula=ClienteCedula).first()
        cliente_existente_email = Client.query.filter_by(ClienteEmail=ClienteEmail).first()
        
        if cliente_existente_cedula:
            message ='Ya existe un CLIENTE registrado con esta CÉDULA', 'warning'
            
        if cliente_existente_email:
            messages_to_flash.append(('Ya existe un CLIENTE registrado con este CORREO ELECTRÓNICO', 'warning'))
            
        if not re.match(r'[^@]+@[^@]+\.[^@]+', ClienteEmail):
            messages_to_flash.append(('Dirección de correo electrónico no válida', 'warning'))
            
        
        if messages_to_flash:
            for message, category in messages_to_flash:
                flash(message, category)
        else:
        # Crea un nuevo objeto Client con los datos del formulario
            nuevo_cliente = Client(ClienteNombre, ClienteCedula, ClienteTel, ClienteEmail, id_services, ClienteComent, ClienteLat, ClienteLon)

        # Agrega y guarda el nuevo cliente en la base de datos
            db.session.add(nuevo_cliente)
            db.session.commit()

            message ='Cliente registrado exitosamente', 'success'
            if origin_page:
                return redirect(url_for('home_BP.' + origin_page),message=message)
    
    # Manejo del método GET
    # Determine qué plantilla HTML renderizar basada en el tipo de usuario o rol
    user_role = session.get('rol')  # Obtén el rol del usuario de la sesión
    if user_role == 1:
        return render_template('addclient_admin.html', pagina_actual=pagina_actual)
    elif user_role == 2:
        return render_template('addclient_ingeniero.html', pagina_actual=pagina_actual)
    elif user_role == 3:
        return render_template('addclient_ventas.html', pagina_actual=pagina_actual)
    elif user_role == 4:
        return render_template('addclient_instalador.html', pagina_actual=pagina_actual)
    else:
        abort(403)  # Acceso prohibido si el rol no está definido

@home_BP.route('/Proyectos/Registro', methods=['GET', 'POST'])
def ClientCrud():
    pagina_actual = 'ClientCrud'
    
    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
        clients = Client.query.filter(
            (Client.ClienteNombre.ilike(f"%{search_term}%")) |
            (Client.ClienteCedula.ilike(f"%{search_term}%")) |
            (Client.ClienteEmail.ilike(f"%{search_term}%"))
        ).all()
        
        return render_template('partials/client_list.html', clients=clients, pagina_actual=pagina_actual)
    
    # Clientes nuevos para el slideshow
    new_clients = Client.query.filter_by(ClienteDone=False).all()
    return render_template('newproject.html', new_clients=new_clients, pagina_actual=pagina_actual)

@home_BP.route('/cliente/<int:client_id>/perfil', methods=['GET'])
def client_profile(client_id):
    pagina_actual = 'ClientCrud'
    client = Client.query.get_or_404(client_id)
    proyectos = Proyecto.query.filter_by(ClientesID=client_id).all()
    return render_template('client_profile.html', client=client, proyectos=proyectos, pagina_actual=pagina_actual)

@home_BP.route('/proyecto/<int:project_id>')
def project_profile(project_id):
    pagina_actual = 'ClientCrud'
    proyecto = Proyecto.query.get_or_404(project_id)
    propuesta = Propuestas.query.filter_by(ProjectID=project_id).first()
    venta = Ventas.query.join(Propuestas).filter(Propuestas.ProjectID == project_id).first()
    proyecto_solar = ProyectoSolar.query.filter_by(ProjectID=project_id).first()

    return render_template(
        'project_profile.html',
        proyecto=proyecto,
        propuesta=propuesta,
        venta=venta,
        proyecto_solar=proyecto_solar,
        pagina_actual=pagina_actual
    )



# Ruta adicional para manejar la búsqueda de clientes con HTMX
@home_BP.route('/search_clients', methods=['POST'])
def search_clients():
    pagina_actual = 'ClientCrud'
    search_term = request.form.get('search_term', '')
    clients = Client.query.filter(
        (Client.ClienteNombre.ilike(f"%{search_term}%")) |
        (Client.ClienteCedula.ilike(f"%{search_term}%")) |
        (Client.ClienteEmail.ilike(f"%{search_term}%"))
    ).all()
    return render_template('partials/client_list.html', clients=clients, pagina_actual=pagina_actual)

@home_BP.route('/cliente/<int:client_id>/nuevo_proyecto')
def SelectAddProject(client_id):
    pagina_actual = 'ClientCrud'
    return render_template('select_project.html', client_id=client_id, pagina_actual=pagina_actual)

@home_BP.route('/cliente/<int:client_id>/nuevo_proyecto/<string:project_type>', methods=['GET', 'POST'])
def AddProject(client_id, project_type):
    pagina_actual = 'ClientCrud'
    client = Client.query.get_or_404(client_id)
    services = Services.query.get(client.id_services)
    message = ''
    if request.method == 'POST':
        try:
            location = request.form['location'].split(',')
            lat = location[0].strip()
            lon = location[1].strip()

            project = Proyecto(
                ClientesID=client_id,
                ClaseID=request.form['claseProyecto'],
                TipoID=1,
                ProjectLat=lat,
                ProjectLon=lon,
                InitDate=request.form['initDate'],
                ProjectName=request.form['ProjectName']
            )

            db.session.add(project)
            db.session.commit()

            solar_project = ProyectoSolar(
                SistemaID=request.form['sistemaSolar'],
                ProjectID=project.ProjectID,
                Demanda=request.form['consumo']
            )
            db.session.add(solar_project)
            db.session.commit()

            # Actualiza ClientDone para el cliente específico
            client.ClienteDone = True
            db.session.commit()

            print(f"Proyecto creado con éxito: {project.ProjectID}")
            flash("Proyecto creado con éxito", "success")
            return redirect(url_for('home_BP.client_profile', client_id=client_id))

        except KeyError as e:
            print(f"Error en el formulario: {e}")
            flash(f"Error en el formulario: {e}", "danger")
        except Exception as e:
            print(f"Error al crear el proyecto: {e}")
            flash(f"Error al crear el proyecto: {e}", "danger")
        
        return redirect(url_for('home_BP.client_profile', client_id=client_id))

    if project_type == 'sistema_fotovoltaico':
        return render_template('sistema_fotovoltaico_form.html', client=client, services=services, pagina_actual=pagina_actual)
    elif project_type == 'automatizacion':
        return render_template('automatizacion_form.html', client=client, services=services, pagina_actual=pagina_actual)
    elif project_type == 'electricidad':
        return render_template('electricidad_form.html', client=client, services=services, pagina_actual=pagina_actual)
    else:
        return "Tipo de proyecto no válido", 404


@home_BP.route('/cotizacion', methods=['GET'])
def Cotizacion():
    pagina_actual = 'Cotizacion'
    proyectos = Proyecto.query.filter_by(CompletadoStatus=False, CanceladoStatus=False).all()
    return render_template('cotizacion.html', proyectos=proyectos, pagina_actual=pagina_actual)

@home_BP.route('/submit_cotizacion', methods=['POST'])
def submit_cotizacion():
    pagina_actual = 'Cotizacion'
    message = ''
    if request.method == 'POST':
        project_id = request.form['project_id']
        propuesta = request.form['propuesta']
        file = request.files['file']

        if not project_id or not propuesta or not file:
            flash('Todos los campos son obligatorios.')
            return redirect(url_for('home_BP.Cotizacion'))

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_COT']
            filepath = os.path.join(upload_folder, filename)
            
            try:
                # Asegúrate de que el directorio de subida existe
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                # Guardar el archivo PDF
                file.save(filepath)

                # Crear un archivo ZIP con el nombre de la propuesta
                zip_filename = secure_filename(propuesta + '.zip')
                zip_filepath = os.path.join(upload_folder, zip_filename)
                
                with zipfile.ZipFile(zip_filepath, 'w') as zipf:
                    zipf.write(filepath, arcname=filename)

                # Eliminar el archivo PDF original después de comprimirlo
                os.remove(filepath)

                # Guardar la cotización en la base de datos
                cotizacion = Propuestas(
                    ProjectID=project_id,
                    Propuesta=propuesta,
                    PropuestaFile=zip_filename
                )
                db.session.add(cotizacion)
                db.session.commit()

                flash('Cotización guardada exitosamente.')
                return redirect(url_for('home_BP.Cotizacion'),pagina_actual=pagina_actual)

            except Exception as e:
                # Si algo falla, eliminar el archivo PDF si existe
                if os.path.exists(filepath):
                    os.remove(filepath)
                flash(f'Ocurrió un error al procesar el archivo: {e}')
                return redirect(url_for('home_BP.Cotizacion'),pagina_actual=pagina_actual)

        flash('El archivo debe estar en formato PDF.')
        return redirect(url_for('home_BP.Cotizacion'),pagina_actual=pagina_actual)

    return redirect(url_for('home_BP.Cotizacion'),pagina_actual=pagina_actual)



@home_BP.route('/datos_mediciones', methods=['GET', 'POST'])
def datos_mediciones():
    pagina_actual = 'datos_mediciones'
    proyectos = Proyecto.query.filter_by(CompletadoStatus=False, CanceladoStatus=False).all()
    
    if request.method == 'POST':
        project_id = request.form['project_id']
        techo_id = request.form['techo_id']
        techo_info = request.form['techo_info']
        aguas = request.form['aguas']
        area_m2 = request.form['area_m2']
        ip_amp = request.form['ip_amp']
        medunits = request.form['medunits']
        medbrand = request.form['medbrand']
        medtipe = request.form['medtipe']
        comentarios = request.form['comentarios']

        # Comprobar si ya existe una entrada para este ProjectID en ProyectoSolar
        proyecto_solar = ProyectoSolar.query.filter_by(ProjectID=project_id).first()
        
        if proyecto_solar:
            # Actualizar los campos existentes
            proyecto_solar.TechoID = techo_id
            proyecto_solar.TechoInfo = techo_info
            proyecto_solar.Aguas = aguas
            proyecto_solar.AreaM2 = area_m2
            proyecto_solar.IpAmp = ip_amp
            proyecto_solar.Medunits = medunits
            proyecto_solar.Medbrand = medbrand
            proyecto_solar.Medtipe = medtipe
            proyecto_solar.Comentarios = comentarios
        else:
            # Crear una nueva entrada si no existe
            proyecto_solar = ProyectoSolar(
                ProjectID=project_id,
                TechoID=techo_id,
                TechoInfo=techo_info,
                Aguas=aguas,
                AreaM2=area_m2,
                IpAmp=ip_amp,
                Medunits=medunits,
                Medbrand=medbrand,
                Medtipe=medtipe,
                Comentarios=comentarios
            )
            db.session.add(proyecto_solar)

        db.session.commit()
        
        flash('Datos de mediciones guardados exitosamente.','success')
        return redirect(url_for('home_BP.datos_mediciones'))

    return render_template('datos_mediciones.html', proyectos=proyectos, pagina_actual=pagina_actual)



@home_BP.route('/planos', methods=['GET'])
def planos():
    pagina_actual = 'planos'
    proyectos_solar = ProyectoSolar.query.join(Proyecto).filter(Proyecto.CompletadoStatus == False, Proyecto.CanceladoStatus == False).all()
    return render_template('planos.html', proyectos=proyectos_solar, pagina_actual=pagina_actual)

@home_BP.route('/submit_planos', methods=['POST'])
def submit_planos():
    pagina_actual = 'planos'
    if request.method == 'POST':
        project_id = request.form['project_id']
        file = request.files['file']


        if not project_id or not file:
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(request.url)

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_PLAN'], filename)
            
            try:
                # Guardar el archivo PDF
                file.save(filepath)

                # Guardar la información del plano en la base de datos
                diseño = Diseño(
                    SolarID=project_id,
                    Planos=filename
                )
                revision = Revision(
                    SolarID=project_id,
                    PapNaturgy= True
                )
                db.session.add(diseño, revision)
                db.session.commit()


                flash('Planos guardados exitosamente.', 'success')
                return redirect(url_for('home_BP.planos'))

            except Exception as e:
                flash(f'Ocurrió un error al procesar el archivo: {e}', 'danger')
                return redirect(request.url)

        flash('El archivo debe estar en formato PDF.', 'danger')
        return redirect(request.url)

    return redirect(url_for('home_BP.planos'))


@home_BP.route('/pre_medidor', methods=['GET'])

def pre_medidor():
    proyectos = Proyecto.query.filter_by(CompletadoStatus=False, CanceladoStatus=False).all()
    return render_template('pre_medidor.html', proyectos=proyectos)

@home_BP.route('/submit_pre_medidor', methods=['POST'])

def submit_pre_medidor():
    if request.method == 'POST':
        project_id = request.form['project_id']
        inversor_config = convert_to_bool(request.form['inversor_config'])
        inversor_log = convert_to_bool(request.form['inversor_log'])
        letrero = convert_to_bool(request.form['letrero'])
        solarname = request.form['solarname']

        # Obtener el proyecto solar correspondiente
        proyecto_solar = ProyectoSolar.query.filter_by(ProjectID=project_id).first()
        proyecto = Proyecto.query.filter_by(ProjectID=project_id).first()

        if proyecto:
            proyecto.CompletadoStatus= True
        db.session.commit()

        if not proyecto_solar:
            flash('Proyecto solar no encontrado.', 'danger')
            return redirect(url_for('home_BP.pre_medidor'))
        else:
            if solarname:
                proyecto_solar.SolarName=solarname
            db.session.commit()

        # Verificar si ya existe una fila de revisión para este SolarID
        revision = Revision.query.filter_by(SolarID=proyecto_solar.SolarID).first()

        if revision:
            revision.InversorConfig=inversor_config
            revision.InversorLog=inversor_log
            revision.letrero=letrero
            flash('Revisión guardada exitosamente.', 'success')
            return redirect(url_for('home_BP.pre_medidor'))
        else:
            # Crear una nueva fila de revisión
            nueva_revision = Revision(
                SolarID=proyecto_solar.SolarID,
                InversorConfig=inversor_config,
                InversorLog=inversor_log,
                letrero=letrero
            )
            db.session.add(nueva_revision)
            db.session.commit()

            flash('Revisión guardada exitosamente.', 'success')
            return redirect(url_for('home_BP.pre_medidor'))

    return redirect(url_for('home_BP.pre_medidor'))


@home_BP.route('/instalacion')
def instalacion():
    pagina_actual = 'install'
    proyectos = Proyecto.query.filter_by(CompletadoStatus=False, CanceladoStatus=False).all()
    paneles = Panel.query.all()
    baterias = Bateria.query.all()
    inversores = Inversores.query.all()
    sistemas = ProyectoSolar.query.all()
    return render_template('instalacion.html', proyectos=proyectos, paneles=paneles, baterias=baterias, inversores=inversores, sistemas=sistemas, pagina_actual=pagina_actual)

@home_BP.route('/submit_instalacion', methods=['POST'])
def submit_instalacion():
    pagina_actual = 'install'
    try:
        project_id = request.form.get('ProjectID')
        capacidad_inst = request.form.get('CapacidadInst')
        panel_id = request.form.get('PanelID')
        panel_watts = request.form.get('PanelWatts')
        panel_units = request.form.get('PanelUnits')
        sistema_id = request.form.get('SistemaID')
        batt_id = request.form.get('BattID') if sistema_id != '2' else None
        batt_watts = request.form.get('BattWatts') if sistema_id != '2' else None
        batt_units = request.form.get('BattUnits') if sistema_id != '2' else None
        data_logger = request.form.get('DataLogger')

        proyecto_solar = ProyectoSolar.query.filter_by(ProjectID=project_id).first()
        
        if proyecto_solar:
            # Actualizar el registro existente
            proyecto_solar.CapacidadInst = capacidad_inst
            proyecto_solar.PanelID = panel_id
            proyecto_solar.PanelWatts = panel_watts
            proyecto_solar.PanelUnits = panel_units
            proyecto_solar.BattID = batt_id
            proyecto_solar.BattWatts = batt_watts
            proyecto_solar.BattUnits = batt_units
            proyecto_solar.DataLogger = data_logger
            
        else:
            # Crear un nuevo registro si no existe
            proyecto_solar = ProyectoSolar(
                ProjectID=project_id,
                CapacidadInst=capacidad_inst,
                PanelID=panel_id,
                PanelWatts=panel_watts,
                PanelUnits=panel_units,
                BattID=batt_id,
                BattWatts=batt_watts,
                BattUnits=batt_units,
                DataLogger=data_logger,
            
            )
            db.session.add(proyecto_solar)
            db.session.flush()  # Generar el SolarID para proyecto_solar



        # Agregar los nuevos inversores
        for i in range(1, 6):
            if request.form.get(f'inversor{i}_enabled'):
                marca_id = request.form.get(f'MarcaID{i}')
                capacidad = request.form.get(f'Capacidad{i}')
                model = request.form.get(f'Model{i}')
                inversor = Inversor(
                    SolarID=proyecto_solar.SolarID,
                    MarcaID=marca_id,
                    Capacidad=capacidad,
                    Model=model
                )
                db.session.add(inversor)

        # Actualizar la fecha de finalización del proyecto
        proyecto = Proyecto.query.get(project_id)
        proyecto.FinishDate = datetime.utcnow()
        
        
        db.session.commit()
        flash('Instalación actualizada con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar la instalación: {str(e)}', 'danger')
    
    return redirect(url_for('home_BP.instalacion'))

def convert_to_bool(value):
    if value in ['1', 'True', True]:
        return True
    return False