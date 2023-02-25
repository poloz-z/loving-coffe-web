import flet 

def main(page: flet.Page):

  page.title = "Amando el Café!"
  page.theme_mode = flet.ThemeMode.LIGHT
  page.padding = 50
  page.fonts = {
      "Pacifico":"/fonts/Pacifico-Regular.ttf",
      "UbuntuNF":"/fonts/Ubuntu-Nerd-Font-Complete.ttf"
      }
  page.update()

  icon_bar = flet.Image(
      src = f"/images/cafe_icon.png",
      width=70,height=70,fit=flet.ImageFit.COVER,
      repeat=flet.ImageRepeat.NO_REPEAT
      )

  appbar = flet.AppBar(
      leading=icon_bar,
      leading_width=70,
      title = flet.Text("Amando cada Día el Café!", color="#313244", size=28,
                        font_family="Pacifico",text_align="start"),
      center_title = False,
      bgcolor = "#ffe9db",
      toolbar_height = 60,
      actions = [
        flet.TextButton(
          content=flet.Text(value="Nosotros", color="#313244",size=18,
                            text_align="center",font_family="UbuntuNF"),
          ),
        flet.TextButton(
          content=flet.Text(value="Productos", color="#313244", size=18,
                            text_align="center",font_family="UbuntuNF"),
          ),
        flet.TextButton(
          content=flet.Text(value="Contactos", color="#313244", size=18,
                            text_align="center",font_family="UbuntuNF"),
          ),
        flet.PopupMenuButton(
          items=[
            flet.PopupMenuItem(text="Objeto 1"),
            flet.PopupMenuItem(),
            ],
          ),
        ],
      )

  page.add(appbar)

if __name__ == "__main__":
  flet.app(port=8226, target=main, view=flet.WEB_BROWSER, assets_dir="recursos")
