import flet as ft

def main(page: ft.Page):
    page.title = "IranFletDev AI"
    page.padding = 20
    page.bgcolor = ft.colors.LIGHT_BLUE_50
    
    # عنوان در بالا
    header = ft.Row(
        [ft.Text("IranFletDev AI", font_family="organical", style="headlineLarge", color="black")],
        alignment="center"
    )
    
    # محتوای چت
    chat_container = ft.Container(
        content=chat,
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=20,
        padding=10,
        expand=True,
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.GREY.with_opacity(0.5),
        ),
    )
    
    # پیام جدید و دکمه ارسال
    input_row = ft.Row(
        [
            new_message,
            ft.IconButton(
                icon=ft.icons.SEND_ROUNDED,
                tooltip="Send message",
                on_click=send_message_click,
                icon_color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE,
                shape=ft.RoundedRectangleBorder(radius=10),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=8,
                    color=ft.colors.GREY.with_opacity(0.4),
                ),
                hover_color=ft.colors.LIGHT_BLUE_100,
            ),
        ],
        alignment="spaceBetween",
        spacing=10,
    )
    
    # افزودن عناصر به صفحه
    page.add(
        header,
        chat_container,
        input_row,
    )

ft.app(port=8550, target=main, view=ft.WEB_BROWSER, assets_dir="assets")
