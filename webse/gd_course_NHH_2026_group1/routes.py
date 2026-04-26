from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from webse.gd_course_NHH_2026_group1.forms import RegistrationForm, LoginForm
from webse import db, bcrypt
from webse.models import User, Route_NHH_2026_g1, Shipment_NHH_2026_g1
from datetime import datetime, timezone
from flask_login import login_required, current_user
from webse.gd_course_NHH_2026_group1.forms import RouteForm, ShipmentForm
from webse.gd_course_NHH_2026_group1.emission_factors import (
    calculate_co2_kg,
    calculate_carbon_cost_nok,
)

gd_course_NHH_2026_group1=Blueprint('gd_course_NHH_2026_group1',__name__)


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/home')
def home_home():
    return render_template('gd_course/NHH_2026_group1/home.html', title='Home')
    
@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/developers')
def developers_home():
    return render_template('gd_course/NHH_2026_group1/developers.html', title='About Us')

@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/methodology')
def methodology_home():
    return render_template('gd_course/NHH_2026_group1/methodology.html', title='Methodology')

@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/register', methods=['GET', 'POST'])
def register():
    # Hvis brukeren allerede er logget inn, gir det lite mening å vise registreringssiden på nytt.
    if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group1.home_home'))
    # Vi oppretter registreringsskjemaet hver gang siden lastes inn.
    form = RegistrationForm()

    # Sender inn skjemaet gitt at alt er fylt ut riktig.
    # validate_username/validate_email i forms.py sjekker allerede om brukernavn/e-post
    # finnes i databasen og kaster ValidationError, så vi trenger ingen ekstra sjekk her.
    if form.validate_on_submit():
        # Passord skal ikke lagres i klartekst, så derfor hasher vi det før vi lagrer brukeren i databasen.
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #Lager selve brukerobjektet.
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, 
                    institution='NHH_2026_group1')

        #Lagrer vi brukeren i databasen.
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('gd_course_NHH_2026_group1.login'))

    # Hvis det bare er vanlig sideinnlasting, eller skjemaet ikke er gyldig,
    # viser vi registreringssiden på nytt.
    return render_template('gd_course/NHH_2026_group1/register.html', title='Register', form=form)


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/login', methods=['GET', 'POST'])
def login():
    # Hvis brukeren allerede er logget inn, sender vi dem tilbake til home.
    if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group1.home_home'))

    # Her oppretter vi innloggingsskjemaet.
    form = LoginForm()

    # Hvis brukeren trykker submit og skjemaet er gyldig
    if form.validate_on_submit():
        # Vi prøver å finne brukeren basert på e-posten som er skrevet inn.
        user = User.query.filter_by(email=form.email.data).first()

        # Hvis brukeren finnes, sjekker vi om passordet stemmer med den lagrede hashen.
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Her skjer selve innloggingen i Flask-Login.
            login_user(user, remember=form.remember.data)

            # Hvis brukeren først prøvde å gå til en beskyttet side,
            # sender vi dem dit etter vellykket login.
            next_page = request.args.get('next')

            flash('You are now logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2026_group1.home_home'))

        # Hvis e-post eller passord ikke stemmer, gir vi feilmelding.
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
            return redirect(url_for('gd_course_NHH_2026_group1.login'))

    # Hvis skjemaet ikke er sendt inn enda, viser vi bare login-siden.
    return render_template('gd_course/NHH_2026_group1/login.html', title='Login', form=form)


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/logout')
@login_required
def logout():
    # Logger ut brukeren og sender dem tilbake til forsiden.
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('gd_course_NHH_2026_group1.home_home'))

# Funksjon A - Rute - Administrasjon
@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/routes/')
@login_required
def your_routes():
    #Bruker klikker eller søker seg frem til "My Routes". Vi må da hente alle routes o
    routes = Route_NHH_2026_g1.query.filter_by(user_id=current_user.id).order_by(Route_NHH_2026_g1.name).all()
    #Etter at vi har hentet alle ruter og lagret de i variablen "routes" henter vi deretter Html
    #filen for "My Routes" og sender med "routes" slik at vi kan vise det for bruker dynamisk.
    return render_template('gd_course/NHH_2026_group1/your_routes.html', title='My Routes', routes=routes)

@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/routes/new', methods=['GET', 'POST'])
@login_required
def new_route():
    #Bruker klikker på "Add New Route". Vi sender bruker videre til et WTForm for å registrere rute.
    form = RouteForm()
    #Hvis bruker klikker submit og det ikke kastes noen feilmeldinger fra validatorene i skjemaet
    #Oppretter vi et Route objekt for å lagre i databasen. 
    if form.validate_on_submit():
        route = Route_NHH_2026_g1(
            name=form.name.data,
            origin=form.origin.data,
            destination=form.destination.data,
            transport_type=form.transport_type.data,
            subcategory=form.subcategory.data,
            distance_km=form.distance_km.data,
            is_active=True,
            user_id=current_user.id
        )
        #Lagrer i database
        db.session.add(route)
        db.session.commit()
        flash('Route added successfully.', 'success')
        #Sender bruker tilbake til "My Routes" siden for bedre brukeropplevelse.
        return redirect(url_for('gd_course_NHH_2026_group1.your_routes'))

    return render_template('gd_course/NHH_2026_group1/new_route.html', title='Add New Route', form=form)


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/routes/toggle/<int:route_id>')
@login_required
def toggle_route(route_id):
    #Bruker klikker "Enable/Disable" på en rute. Vi henter kun ruten hvis den tilhører innlogget bruker.
    route = Route_NHH_2026_g1.query.filter_by(id=route_id, user_id=current_user.id).first_or_404()
    #Flipper is_active-feltet (True -> False eller False -> True)
    route.is_active = not route.is_active
    #Sender endringen til databasen. Når vi da henter ny visning av HTML "My routes" blir den oppdatert
    db.session.commit()
    #Gir bruker tilbakemelding avhengig av ny status, og sender tilbake til ruteoversikten.
    flash('Route enabled.' if route.is_active else 'Route disabled.',
          'success'        if route.is_active else 'warning')
    
    return redirect(url_for('gd_course_NHH_2026_group1.your_routes'))


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/routes/delete/<int:route_id>')
@login_required
def delete_route(route_id):
    #Bruker klikker "Delete" på en rute. Vi henter kun ruten hvis den tilhører innlogget bruker.
    route = Route_NHH_2026_g1.query.filter_by(id=route_id, user_id=current_user.id).first_or_404()

    #Vi teller shipments på ruten med pythoh .count() og blokkerer sletting hvis det finnes noen.
    shipment_count = Shipment_NHH_2026_g1.query.filter_by(route_id=route.id).count()
    if shipment_count > 0:
        flash(
            f'Cannot delete "{route.name}" — it has {shipment_count} '
            f'logged shipment(s). Deactivate it instead.',
            'warning'
        )
        return redirect(url_for('gd_course_NHH_2026_group1.your_routes'))
    
    #Ingen tilknyttede shipments, ergo det trygt å slette ruten.
    db.session.delete(route)
    db.session.commit()
    flash('Route deleted.', 'success')
    return redirect(url_for('gd_course_NHH_2026_group1.your_routes'))

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# Funksjon B — Loggføre shipments
@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/shipments/new', methods=['GET', 'POST'])
@login_required
def new_shipment():
    #Bruker klikker på "Log New Shipment". Vi sender bruker videre til et WTForm for å registrere rute.
    form = ShipmentForm()
    #Henter alle aktive routes for bruker som er innlogget
    active_routes = Route_NHH_2026_g1.query.filter_by(user_id=current_user.id, is_active=True).all()
    form.route_id.choices = [
        (route.id, f"{route.name} ({route.origin} → {route.destination})") for route in active_routes
    ]

    if request.method == 'GET':
        form.shipped_at.data = datetime.now(timezone.utc).date()

    if form.validate_on_submit():
        route = Route_NHH_2026_g1.query.get_or_404(form.route_id.data) #Hente tilhørende ID for valgt Route
        #Mellomlagre variabler fra route som bruker har valgt for å beregne co2 og carbon cost.
        kms = route.distance_km
        weight = form.cargo_tonnes.data
        fuel = form.fuel_type.data
        transport = route.transport_type  # Må matche toppnivånøkkel i EMISSION_FACTORS_CO2: "Road" | "Sea" | "Air"
        subcat = route.subcategory        # Må matche undernøkkel i EMISSION_FACTORS_CO2 — garantert av validate_subcategory i forms.py
        #Beregne co2 og carbon cost med python funksjoner (se emission_factors.py)
        co2_kg          = round(calculate_co2_kg(transport, subcat, fuel, kms, weight), 4)
        carbon_cost_nok = round(calculate_carbon_cost_nok(co2_kg), 2)

        #Opprette Shipment objektet vi skal logge i databasen 
        shipment = Shipment_NHH_2026_g1(
            cargo_tonnes=weight,
            fuel_type=fuel,
            co2_kg=co2_kg,
            carbon_cost_nok=carbon_cost_nok,
            shipped_at=form.shipped_at.data,
            route_id=route.id,
            user_id=current_user.id
        )
        #Lagre Shipment objektet
        db.session.add(shipment)
        db.session.commit()
        flash('Shipment logged successfully.', 'success')
        return redirect(url_for('gd_course_NHH_2026_group1.your_shipments'))

    return render_template('gd_course/NHH_2026_group1/new_shipment.html', title='Log New Shipment', form=form, active_routes=active_routes)


# Funksjon C — Administrere shipments
@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/shipments/')
@login_required
def your_shipments():
    #Bruker klikker på "My Shipments". Vi henter derfor alle shipments for bruker og sender til HTML.
    #Templaten bruker entry.route.<felt> via SQLAlchemy backref for å vise rute-info per shipment.
    entries = Shipment_NHH_2026_g1.query.filter_by(user_id=current_user.id).order_by(Shipment_NHH_2026_g1.shipped_at.desc()).all()
    return render_template('gd_course/NHH_2026_group1/your_shipments.html', title='My Shipments', entries=entries)


@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/shipments/delete/<int:entry_id>')
@login_required
def delete_shipment(entry_id):
    #Bruker klikker "Delete" på en shipment. Vi henter kun oppføringen hvis den tilhører innlogget bruker.
    entry = Shipment_NHH_2026_g1.query.filter_by(id=entry_id, user_id=current_user.id).first_or_404()

    #Sletter shipment som bruker velger.
    db.session.delete(entry)
    db.session.commit()
    flash('Shipment deleted.', 'success')
    return redirect(url_for('gd_course_NHH_2026_group1.your_shipments'))

@gd_course_NHH_2026_group1.route('/green_digitalization_course/NHH/2026/group1/carbon_app/your_data')
@login_required
def your_data_home():
    # STEG 1: Hent all data fra databasen for den innloggede brukeren
    # Vi henter BÅDE shipments og routes fordi dashboardet skal vise:
    #   - statistikk basert på shipments (CO2, kostnad, osv.)
    #   - antall aktive ruter (fra routes)
    shipments = Shipment_NHH_2026_g1.query.filter_by(user_id=current_user.id).all()
    routes = Route_NHH_2026_g1.query.filter_by(user_id=current_user.id).all()


    # STEG 2: Håndter tom-tilstand (bruker har ikke logget noen shipments enda)
    # Hvis brukeren ikke har noen shipments, har vi ingenting å regne på.
    # Vi sender da has_data=False til templaten, som viser en "empty state"
    # melding (se your_data.html linje 17-21: "You haven't logged any shipments yet").
    # "return" her gjør at resten av funksjonen IKKE kjøres.
    if len(shipments) == 0:
        return render_template(
            'gd_course/NHH_2026_group1/your_data.html',
            title='Your Data',
            has_data=False
        )
    # Hvis koden kommer hit, har brukeren minst én shipment og vi kan regne ut statistikk:

    # STEG 3: Regn ut de fire KPI-tallene som vises øverst på dashboardet
    # Totalt antall shipments brukeren har logget
    total_shipments = len(shipments)

    # Summer opp CO2 fra alle shipments.
    # Vi starter på 0 og legger til co2_kg for hver shipment i en løkke.
    total_co2_kg = 0
    for s in shipments:
        total_co2_kg = total_co2_kg + s.co2_kg
    total_co2_tonnes = round(total_co2_kg / 1000, 2) #KONVERT TIL TONN

    # Summer opp karbonkostnaden fra alle shipments på samme måte
    total_carbon_cost_nok = 0
    for s in shipments:
        total_carbon_cost_nok = total_carbon_cost_nok + s.carbon_cost_nok
    total_carbon_cost_nok = round(total_carbon_cost_nok, 2)

    # Summer opp total godsmengde (i tonn) fra alle shipments
    total_cargo_tonnes = 0
    for s in shipments:
        total_cargo_tonnes = total_cargo_tonnes + s.cargo_tonnes
    total_cargo_tonnes = round(total_cargo_tonnes, 1)

    # Tell hvor mange ruter som er aktive (is_active = True)
    active_routes_count = 0
    for r in routes:
        if r.is_active == True:
            active_routes_count = active_routes_count + 1


    # STEG 4: Aggreger utslipp og kostnad per transporttype (Road / Sea / Air)
    # Vi skal vise en tabell og et donut-diagram som sammenligner transporttypene.
    # For å gjøre det trenger vi totaler per type.
    
    # Vi bruker en dictionary (transport_totals) hvor:
    #   - NØKKEL er transporttype-navnet, f.eks. "Road"
    #   - VERDI er en dict med {'co2_kg': ..., 'cost_nok': ..., 'shipments': ...}
    #
    # Vi må bruke s.route.transport_type fordi transporttypen ligger på Route,
    # ikke direkte på Shipment. SQLAlchemy-backref lar oss hoppe fra shipment
    # til tilhørende route med s.route.

    transport_totals = {}

    for s in shipments:
        # Hent transporttypen til denne shipment'en via ruten
        transport_type = s.route.transport_type

        # Hvis dette er første gang vi ser denne transporttypen, lag en ny tom oppføring
        if transport_type not in transport_totals:
            transport_totals[transport_type] = {
                'co2_kg': 0,
                'cost_nok': 0,
                'shipments': 0
            }

        # Legg til tallene fra denne shipment'en i totalen for transporttypen
        transport_totals[transport_type]['co2_kg'] = transport_totals[transport_type]['co2_kg'] + s.co2_kg
        transport_totals[transport_type]['cost_nok'] = transport_totals[transport_type]['cost_nok'] + s.carbon_cost_nok
        transport_totals[transport_type]['shipments'] = transport_totals[transport_type]['shipments'] + 1

    # STEG 5: Konverter dictionary'en til en liste som templaten kan løkke over
    # Jinja2 (Flask sin template-motor) håndterer lister av dicts bedre enn
    # nested dicts i for-løkker. Vi lager derfor en liste by_transport hvor
    # hver oppføring er en dict som beskriver én transporttype.
    # Samtidig regner vi ut prosent-andelen av total CO2 for hver type.

    by_transport = []

    for transport_type in transport_totals:
        # Hent ut verdiene for denne transporttypen
        vals = transport_totals[transport_type]

        # Regn ut prosent-andel av total CO2.
        # VIKTIG: Hvis alle shipments har co2_kg = 0 (f.eks. bruker kun "No Fossil Fuel"),
        # vil total_co2_kg være 0, og da får vi division-by-zero feil.
        # Derfor sjekker vi først om total_co2_kg er større enn 0.
        if total_co2_kg > 0:
            share_pct = round(vals['co2_kg'] / total_co2_kg * 100, 0)
        else:
            share_pct = 0

        # Lag én oppføring i listen for denne transporttypen
        by_transport.append({
            'transport_type': transport_type,
            'co2_kg': round(vals['co2_kg'], 1),
            'co2_tonnes': round(vals['co2_kg'] / 1000, 2),
            'cost_nok': round(vals['cost_nok'], 2),
            'shipments': vals['shipments'],
            'share_pct': share_pct,
        })

    # Sorter listen slik at transporttypen med MEST CO2 kommer først.
    # reverse=True betyr synkende rekkefølge (størst først).
    by_transport.sort(key=lambda x: x['co2_kg'], reverse=True)


    # STEG 6: Bygg data i riktig format for Chart.js donut-diagrammet
    # Chart.js trenger to parallelle lister:
    #   - emission_labels: navnene som skal vises i diagrammet
    #   - emission_data: tallverdiene (CO2 i tonn)
    #
    # Rekkefølgen må være FAST og lik i begge listene, ellers kommer
    # feil label på feil verdi. Derfor bygger vi dem eksplisitt fra
    # en fast liste med transport_keys.
    #
    # Fast rekkefølge vi ønsker å vise transporttypene i.
    # Labels matcher tabellen ved siden av diagrammet (Road/Sea/Air).
    transport_keys = ['Road', 'Sea', 'Air']
    emission_labels = ['Road', 'Sea', 'Air']

    # Lag et oppslag fra transporttype til tonn CO2 (fra by_transport som vi lagde over)
    transport_lookup = {}
    for item in by_transport:
        transport_lookup[item['transport_type']] = item['co2_tonnes']

    # Bygg emission_data i samme rekkefølge som transport_keys/emission_labels.
    # Hvis brukeren ikke har noen shipments for en transporttype, settes verdien til 0.
    emission_data = []
    for key in transport_keys:
        if key in transport_lookup:
            emission_data.append(transport_lookup[key])
        else:
            emission_data.append(0)


    # STEG 7: Finn de 5 rutene som har mest CO2-utslipp totalt
    # Samme teknikk som for transport_totals, men nå grupperer vi per rute-ID
    # istedenfor transporttype. Vi må lagre navn/origin/destination siden
    # vi skal vise dem i tabellen.

    route_totals = {}

    for s in shipments:
        # Hent ID'en til ruten denne shipment'en tilhører
        rid = s.route.id

        # Første gang vi ser denne ruten: lag en ny oppføring med rutedetaljer
        if rid not in route_totals:
            route_totals[rid] = {
                'name': s.route.name,
                'origin': s.route.origin,
                'destination': s.route.destination,
                'co2_kg': 0,
                'shipments': 0,
            }

        # Legg til denne shipment'ens CO2 og tell opp antall shipments for ruten
        route_totals[rid]['co2_kg'] = route_totals[rid]['co2_kg'] + s.co2_kg
        route_totals[rid]['shipments'] = route_totals[rid]['shipments'] + 1

    # Hent ut alle rute-oppføringene som en liste (vi trenger ikke ID'en lenger,
    # bare verdiene), og sorter med høyest CO2 først.
    all_routes_sorted = sorted(
        route_totals.values(),
        key=lambda r: r['co2_kg'],
        reverse=True
    )

    # Ta kun de 5 første (topp 5). [:5] betyr "de første 5 elementene i listen".
    top_routes = all_routes_sorted[:5]

    # Rund av CO2-verdien til 1 desimal for penere visning i tabellen
    for r in top_routes:
        r['co2_kg'] = round(r['co2_kg'], 1)


    # STEG 8: Finn de 5 nyeste shipments (sortert på dato)
    # Sorter shipments-listen etter dato, nyeste først, og ta de 5 første.
    # s.shipped_at er en date-verdi, så sortering fungerer naturlig på dato.
    recent_shipments = sorted(
        shipments,
        key=lambda s: s.shipped_at,
        reverse=True
    )[:5]


    # STEG 9: Send all utregnet data til templaten for visning
    # render_template tar templatenavnet først, og deretter alle variablene
    # som templaten skal få tilgang til som "keyword arguments" (navn=verdi).
    # has_data=True signaliserer at vi har data å vise (ikke empty state).
    return render_template(
        'gd_course/NHH_2026_group1/your_data.html',
        title='Your Data',
        has_data=True,
        total_shipments=total_shipments,
        total_co2_tonnes=total_co2_tonnes,
        total_carbon_cost_nok=total_carbon_cost_nok,
        total_cargo_tonnes=total_cargo_tonnes,
        active_routes_count=active_routes_count,
        by_transport=by_transport,
        top_routes=top_routes,
        recent_shipments=recent_shipments,
        emission_labels=emission_labels,
        emission_data=emission_data,
    )
