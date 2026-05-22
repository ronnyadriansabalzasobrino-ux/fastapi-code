def build_email(titulo: str, mensaje: str, detalle: str = ""):
    import base64
    logo_path = "app/assets/logo.png"
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode('utf-8')
        
    return f"""
    <div style="font-family: Arial, sans-serif; background:#f4f6f9; padding:30px;">

        <!-- HEADER -->
        <div style="max-width:600px; margin:auto; background:#2a5298; padding:20px; border-radius:12px 12px 0 0; text-align:center;">
           {"<img src='data:image/png;base64," + logo_base64 + "' style='width:60px; margin-bottom:10px;'>" if logo_base64 else ""}
            <h2 style="color:white; margin:0;">School System</h2>
        </div>

        <!-- BODY -->
        <div style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:0 0 12px 12px;">

            <h2 style="color:#2a5298;">{titulo}</h2>

            <p style="font-size:16px; color:#333;">
                {mensaje}
            </p>

            <div style="background:#f4f6f9; padding:15px; border-radius:10px; margin-top:20px;">
                {detalle}
            </div>

            <p style="margin-top:30px; font-size:12px; color:#999;">
                Este es un mensaje automático del sistema académico.
            </p>

        </div>

    </div>
    """