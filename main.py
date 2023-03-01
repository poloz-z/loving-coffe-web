import flet
from data_base import DataBase 

def main(page: flet.Page):

    #data = DataBase()

    page.title = "Amando el café"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.theme_mode = flet.ThemeMode.LIGHT
    page.padding = 50
    page.vertical_alignment = "center"
    page.horizontal_alignment = "left"
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
            if data.user_auth(usuario.current.value, passw.current.value): 
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
        if nombre.current.value == "" or correo.current.value == "" or passwo.current.value == "":
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
                flet.TextButton(on_click=lambda x:page.go("/sobre"),
                  content=flet.Text(value="Nosotros", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                flet.TextButton(on_click=lambda x:page.go("/productos"),
                  content=flet.Text(value="Productos", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                flet.TextButton(on_click=lambda x:page.go("/contactos"),
                  content=flet.Text(value="Contactos", color="#313244",size=15,text_align="center",font_family="UbuntuNF"),),
                flet.PopupMenuButton(
                  items=[
                    flet.PopupMenuItem(text="Cerrar"),
                  ],
                ), 
            ],
        )

    def route_cambio(e):
      page.views.clear()
      page.views.append(
        flet.View(
          "/",
          [
            login,
            appbar,
            flet.Text("Main"),
            flet.Column(ref=geeting)
          ],
        )
      )

      if page.route == "/sobre":
        page.views.clear()
        page.views.append(
          flet.View(
            "/sobre",
              [
                appbar,
                flet.Text("Sobre")
              ],
            )
        )

      if page.route == "/productos":
            page.views.clear()
            page.views.append(
              flet.View(
                "/productos",
                  [
                    appbar,
                    flet.Text("Productos")
                  ],
            )
        )

      if page.route == "/contactos":
            page.views.clear()
            page.views.append(
              flet.View(
                "/contactos",
                [
                  appbar,
                  flet.Text("Contactos")
                ],
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
   flet.app(port=8662, target=main, view=flet.WEB_BROWSER, assets_dir="recursos")
