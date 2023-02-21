import flet 

def main(page: flet.Page):

  appbar = flet.AppBar(
      title = flet.Text("Amando el Café", color="white", size=35),
      bgcolor = "brown"
      )

  page.add(appbar)

if __name__ == "__main__":
  flet.app(port=8226, target=main, view=flet.WEB_BROWSER)
