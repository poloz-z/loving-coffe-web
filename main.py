import flet
from data_base import DataBase 

sobre_m = """
# EMPRESA __“AMANDO CADA DIA EL CAFÉ”__
## Rif; J XXX XXX

__REGISTRO:__ En trámite de su registro por el _“Servicio Autónomo de Registros y Notarías”_ (SAREN) fue gestionado para ser una empresa legal de acuerdo para poder aprobar dicho nombre llamado __“Amando Cada Día el Café”__ para su registro único para poder proceder a su redacción del acta constitutiva por parte de las leyes puedan ser aprobado por las clausulas que conforma el documento de la empresa; 
Por parte su objetivo es tener mayor producción con el 60% a invertir llegando a una meta de lograr que sea exitosa su producción a un 100%

__OBJETIVO (COMO EMPRESA DE PRODUCCION):__  Su objetivo es tener calidad de producto para llegar ser una marca “Reconocida” para el cliente y desarrollar su producción exitosamente a un 100% de producción. 

__COMERCIO Y VENTAS:__  Para comercializar y poder ser una grande empresa, está deberá comercializar el café como un producto interno bruto, de esta manera poder producir, distribuir y ofertar está marca. Para satisfacer las necesidades y expectativas de los consumidores con la mejor calidad y la mejor relación precio/ venta. 

__PERSONAL:__ La empresa esta conformada por un grupo de 26 personas donde gracias a ellos la empresa va creciendo poco a poco por parte de su producción a diario.
"""


def main(page: flet.Page):

    #data = DataBase()

    page.title = "Amando el café"
    show_semantics_debugger = True
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.theme_mode = flet.ThemeMode.LIGHT
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.fonts = {"Pacifico":"/fonts/Pacifico-Regular.ttf","UbuntuNF":"/fonts/Ubuntu-Nerd-Font-Complete.ttf"}
    page.update()

    # VARIABLES DE ENTORNO
    geeting = flet.Ref[flet.Column]()

    usuario = flet.Ref[flet.TextField]()
    passw = flet.Ref[flet.TextField]()

    correo = flet.Ref[flet.TextField]()
    nombre = flet.Ref[flet.TextField]()
    passwo = flet.Ref[flet.TextField]()

    # LOG IN AND SIGN IN FUNCTIONS
    def login_s(e):
        if usuario.current.value == "" or passw.current.value == "":
            usuario.current.error_text = "Ingrese un usuario"
            passw.current.error_text = "Ingrese una contraseña"
            page.update()
        else:
            data = DataBase()
            if data.user_query(usuario.current.value) == usuario.current.value and data.pass_query(passw.current.value) == passw.current.value: 
                login.open = False
                page.update()
            else:
                usuario.current.error_text = "Usuario u contraseña incorrecta"
                passw.current.error_text = "Usuario u contraseña incorrecta"
                page.update()


    def registro_s(e):
        login.open = False
        page.dialog = registro
        registro.open = True
        page.update()

    def registro_c(e):
       # if nombre.current.value == "" or correo.current.value == "" or passwo.current.value == "":
       if data.user_auth(usuario.current.value, passw.current.value): 
          nombre.current.error_text = "Ingrese el nombre de usuario" 
          correo.current.error_text = "Ingrese el correo"
          passwo.current.error_text = "Ingrese su clave"
          page.update()

        else:
          data = DataBase()
          data.add_user(nombre.current.value,correo.current.value,passwo.current.value)
          registro.open = False
          page.update()

    registro = flet.AlertDialog(
      modal = True,
      open = True,
      title = flet.Text("Registro"),
      content = flet.Column([
          flet.TextField(ref=nombre,label="Nombre",autofocus=True),
          flet.TextField(ref=correo,label="Correo",suffix_text=".com"),
          flet.TextField(ref=passwo,label="Contraseña",password=True,can_reveal_password=True)
          ]),
      actions = [flet.ElevatedButton("Registrarse", on_click=registro_c)]
    ) 

    login = flet.AlertDialog(
      modal = True,
      open = True,
      title=flet.Text("Ingresar"),
      content= flet.Column([
        flet.TextField(ref=usuario,label="Usuario",autofocus=True),
        flet.TextField(ref=passw,label="Contraseña",password=True,can_reveal_password=True)
      ]),
      actions=[
        flet.Container(
          content=flet.Row([
          flet.ElevatedButton("Ingresar",on_click=login_s),
          flet.ElevatedButton("Registrarse",on_click=registro_s)
        ],
        tight=True),
        alignment=flet.alignment.center)
      ]
    )
    
    #TITLE BAR 
    image = flet.Image(
            src = f"/images/cafe_icon.png",
            width = 65,
            height = 65,
            fit = flet.ImageFit.COVER,
            repeat=flet.ImageRepeat.NO_REPEAT,
            #border_radius=flet.border_radius.all(10),
            )

    appbar = flet.AppBar(
            leading=image,
            leading_width=60,
            title =  flet.TextButton(on_click=lambda x:page.go("/"),
                content=flet.Text("Amando cada Día el Café!", color="#313244",size=23, font_family="Pacifico", text_align="start"),),
            center_title = False,
            bgcolor = "#ffe9db",
            toolbar_height = 55,
            actions = [
                flet.PopupMenuButton(
                  icon = flet.icons.MENU_OUTLINED,
                  items = [
                    flet.PopupMenuItem(on_click=lambda x:page.go("/sobre"),icon = flet.icons.PEOPLE,text="Nosotros"),
                        #content=flet.Text(value="Nosotros", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                    flet.PopupMenuItem(on_click=lambda x:page.go("/productos"), icon = flet.icons.COFFEE_ROUNDED,text="Productos"),
                        #content=flet.Text(value="Productos", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                    flet.PopupMenuItem(on_click=lambda x:page.go("/contactos"), icon = flet.icons.CONTACT_PAGE,text="Contactos"),
                        #content=flet.Text(value="Contactos", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                ]
              )
            ]
        )

    main_image = flet.Image(
            src = f"/images/cafe_img.png",
            width = 300, height = 300,
            fit = flet.ImageFit.SCALE_DOWN,
            repeat = flet.ImageRepeat.NO_REPEAT,
            border_radius=500
            )

    cool = flet.Column(spacing=40)

    main_text = flet.Column([
                flet.Text(value="Bienvenido a Amando Cada Día al Café!",font_family="UbuntuNF",size=30, text_align = "center",weight = flet.FontWeight.W_600),
                flet.Text(value="Somos una pequeña empresa cafetera que busca ser la mayor productora a nivel nacional, nuestros productos brindaran el mejor Café para nuestros hermanos Venezolano y en un futuro cercano a las personas del mundo, nuestros granos han sido seleccionados con la mayor calidad y nuestro café preparado con todo el amor que se necesita para beber una buena taza de Café que Amaremos Cada Día Mas~!."
                          ,size=17,style=flet.TextThemeStyle.BODY_SMALL)],spacing=30)

    buttom_text = flet.Text(value="Copyright - 2023 Amando Cada Día el Café Inc. Build with Flet",font_family="UbuntuNF")

    contenedor_main = flet.Container(
        content=main_text,
        padding=30,
        bgcolor = "#bab3cb",
        border_radius = 60,
        margin = flet.margin.symmetric(vertical=40)
    )

    #SOBRE

    markdown = flet.Markdown(sobre_m,extension_set="gitHubWeb")

    sobre_content = flet.Column([
        markdown
        ],spacing=60)

    sobre_main = flet.Container(
        content=sobre_content,
        padding=50,
        bgcolor="#bab3cb",
        border_radius= 40,
        margin = flet.margin.symmetric(vertical=50),
        alignment = flet.alignment.center,
        ) 

    #PRODUCTOS 

    def init_compra(e):
        page.dialog = compra
        compra.open = True
        page.update()

    def compra_c(e):
        compra.open = False
        page.update()

    compra = flet.AlertDialog(
            title = flet.Text("COMPRA EXITOSA"),
            modal = False,
            content = flet.ElevatedButton("Listo",on_click=compra_c)
            )

    granos_img = flet.Image(
            src = f"/images/cafe_granos.png"
            )

    venta_content = flet.Column([
        flet.Text(value="Café en Granos:",size=35,font_family="UbuntuNF",text_align="center",weight=flet.FontWeight.W_800),
        granos_img,
        flet.Text(value="Los mejores granos de café, cultivados y cocechado por proveedores de confianza, para preparar el mas delicioso café.",
                  size=18,text_align="center"),
        flet.TextField(label="Ingrese la calidad de kilos de Café a comprar",autofocus=True),
        flet.ElevatedButton("Comprar",on_click=init_compra),
        ],spacing=20)

    venta = flet.Container(
            content=venta_content,
            padding=25,
            bgcolor="#bab3cb",
            border_radius = 20,
            alignment = flet.alignment.center,
            margin = flet.margin.symmetric(vertical=20)
            )

    # CONTACTOS
    
    taza_img = flet.Image(src=f"/images/taza_cafe.png",width=100,height=100)

    contactos_content = flet.Column([
        flet.Text(value="Instagram: @amando_elcafe",size=20),
        flet.Text(value="Facebook: Amando Cada Día el Café",size=20),
        flet.Text(value="Twitter: @Amandocadadiaelcafe_5",size=20),
        ],spacing=20)

    contactos = flet.Container(
            content=contactos_content,
            padding=40,
            bgcolor="#bab3cb",
            border_radius=60,
            )

    def route_cambio(e):
      page.views.clear()
      page.views.append(
        flet.View(
          controls = [
            login,
            contenedor_main,
            main_image,
            buttom_text
          ],
          route = "/",
          appbar = appbar,
          spacing = 10,
          scroll = flet.ScrollMode.ALWAYS,
          horizontal_alignment = flet.CrossAxisAlignment.CENTER,
          vertical_alignment = flet.MainAxisAlignment.CENTER,
        )
      )

      if page.route == "/sobre":
        page.views.clear()
        page.views.append(
          flet.View(
              route = "/sobre",
              controls = [
               flet.Text(value="SOBRE NUESTRA EMPRESA",size=42,font_family="UbuntuNF",weight=flet.FontWeight.W_800,text_align="center"),
               sobre_main,
               buttom_text
              ],
              appbar = appbar,
              padding = 40,
              spacing = 20,
              scroll = "always",
              horizontal_alignment = flet.CrossAxisAlignment.CENTER,
              vertical_alignment = flet.MainAxisAlignment.CENTER,
            )
        )

      if page.route == "/productos":
            page.views.clear()
            page.views.append(
              flet.View(
                route = "/productos",
                controls = [
                    flet.Text(value="PRODUCTOS",size=42,font_family="UbuntuNF",weight=flet.FontWeight.W_800,text_align="center"),
                    main_image,
                    venta,
                    buttom_text
                ],
                appbar = appbar,
                scroll = "always",
                spacing = 40,
                horizontal_alignment = flet.CrossAxisAlignment.CENTER,
                vertical_alignment = flet.MainAxisAlignment.CENTER,
            )
        )

      if page.route == "/contactos":
            page.views.clear()
            page.views.append(
              flet.View(
                route = "/contactos",
                controls = [
                  flet.Text(value="NUESTROS CONTACTOS",size=42,font_family="UbuntuNF",weight=flet.FontWeight.W_800,text_align="center"),
                  contactos,
                  taza_img,
                  buttom_text
                ],
                appbar = appbar,
                scroll = "always",
                spacing = 40,
                horizontal_alignment = flet.CrossAxisAlignment.CENTER,
                vertical_alignment = flet.MainAxisAlignment.CENTER,
            )
        )  

    def ver_pop(e):
      page.views.pop()
      top_view = page.views[-1]
      page.go(top_view.route)

    page.on_route_change = route_cambio
    page.on_view_pop = ver_pop

    page.go(page.route)

if __name__ == "__main__":
   flet.app(port=8662, target=main, view=flet.WEB_BROWSER, assets_dir="recursos", web_renderer="auto", route_url_strategy="hash")
