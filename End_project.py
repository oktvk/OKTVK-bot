from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler

key_token = "6859220883:AAFtT6yjdA-WGtpsnUIiKmDyxfjBSOU7PMM" #Masukkan KEY-TOKEN BOT 
user_bot = "Okstvk_bot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Okstvk_bot silahkan coba command /help untuk melihat list command")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan.. \ncommand list :\n1. halo\n2. apa fungsi kamu?\n3. siapa kamu? \n4. tolong rekomendasikan VGA untuk harga (1-5) juta\n5. tolong rekomendasikan CPU untuk harga (1-5) juta\n6. tolong rekomendasikan MOBO (AMD (AM4/AM5)/ INTEL)")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima:
        await update.message.reply_text("Hallo silahkan masukan command")
    elif 'apa fungsi kamu?' in text_lwr_diterima:
        await update.message.reply_text("Fungsi ku adalah : merekomendasikan komponen pc seperti VGA, CPU, dan MOBO untuk pc build anda")
#VGA
    elif 'tolong rekomendasikan vga untuk harga 1 juta' in text_lwr_diterima:
        await update.message.reply_text("untuk harga 1 jtan, ada beberapa VGA yang bisa kamu beli ,Tetapi saya merekomendasikan RX 560 VGA ini dibuat oleh AMD pada tahun 2017 memiliki 4 GB DDR5 VRAM| Video output function :HDMI, DVI-D, HDCP support, Display port(tergantung model)|minimum power requirement yang tergolonng kecil yaitu 300 Watt")
    elif 'tolong rekomendasikan vga untuk harga 2 juta' in text_lwr_diterima:
        await update.message.reply_text("untuk harga 2 jtan, ada beberapa VGA yang bisa kamu beli ,Tetapi saya merekomendasikan GTX 1660 Ti VGA ini dibuat oleh NVIDIA pada tahun 2019 memiliki 6 GB GDDR6 VRAM| Video outpuut function :HDMI, DVI-D, HDCP support, Display port(tergantung model)|minimum power requirement yang tergolong kecil yaitu 350 Watt")
    elif 'tolong rekomendasikan vga untuk harga 3 juta' in text_lwr_diterima:
        await update.message.reply_text("untuk harga 3 jtan, ada beberapa VGA yang bisa kamu beli ,Tetapi saya merekomendasikan Radeon RX 6650 XT VGA ini dibuat oleh AMD pada tahun 2022 memiliki 8 GB GDDR6 VRAM| Video outpuut function :HDMI, Display port(tergantung model)|minimum power requirement yang tergolong menengah yaitu 500 Watt")
    elif 'tolong rekomendasikan vga untuk harga 4 juta' in text_lwr_diterima:
        await update.message.reply_text("untuk harga 4 jtan, ada beberapa VGA yang bisa kamu beli ,Tetapi saya merekomendasikan RTX 3060 VGA ini dibuat oleh NVIDIA pada tahun 2021 memiliki 8 - 12 GB GDDR6 VRAM(tergantung model)| Video outpuut function :HDMI, Display port(tergantung model)|minimum power requirement yang tergolong menengah yaitu 550 Watt")
    elif 'tolong rekomendasikan vga untuk harga 5 juta' in text_lwr_diterima:
        await update.message.reply_text("untuk harga 5 jtan, ada beberapa VGA yang bisa kamu beli ,Tetapi saya merekomendasikan Radeon  RX 6700 XT VGA ini dibuat oleh AMD pada tahun 2021 memiliki 12 GB GDDR6 VRAM| Video outpuut function :HDMI, Display port(tergantung model)|minimum power requirement yang tergolong sedikit tinggi yaitu 650 Watt")
#CPU
    elif 'tolong rekomendasikan cpu untuk harga 1 juta' in text_lwr_diterima:
        await update.message.reply_text("Untuk harga 1 jutaan, saya dapat merekomendasikan INTEL i3-12100F CPU ini dibuat oleh INTEL pada tahun 2021 dengan socket LGA1700 |memiliki 4 core dan 8  dengan socket LGA1700 threads | frequency 3.30 - 4.30 GHz| base power : 58 W ")
    elif 'tolong rekomendasikan cpu untuk harga 2 juta' in text_lwr_diterima:
        await update.message.reply_text("Untuk harga 2 jutaan, saya dapat merekomendasikan Ryzen 5600 CPU ini dibuat oleh AMD pada tahun 2022 dengan socket AM4  |memiliki 6 core dan 12  threads | frequency 3.50 - 4.40 GHz| base power : 65 W ")
    elif 'tolong rekomendasikan cpu untuk harga 3 juta' in text_lwr_diterima:
        await update.message.reply_text("Untuk harga 3 jutaan, saya dapat merekomendasikan INTEL i5-13400F CPU ini dibuat oleh INTEL pada tahun 2022 dengan socket  LGA1700  |memiliki 10 core dan 16  threads | frequency 2.50 - 4.60 GHz| base power : 65 W ")
    elif 'tolong rekomendasikan cpu untuk harga 4 juta' in text_lwr_diterima:
        await update.message.reply_text("Untuk harga 4 jutaan, saya dapat merekomendasikan INTEL i7-12700F CPU ini dibuat oleh INTEL pada tahun 2021 dengan socket  LGA1700  |memiliki 12 core dan 20  threads | frequency 2.10 - 4.90 GHz| base power : 65 W ")
    elif 'tolong rekomendasikan cpu untuk harga 5 juta' in text_lwr_diterima:
        await update.message.reply_text("Untuk harga 5 jutaan, saya dapat merekomendasikan  Ryzen 7700X CPU ini dibuat oleh INTEL pada tahun 2022 dengan socket  AM5  |memiliki 8 core dan 16  threads | frequency 4.50 - 5.40 GHz| base power : 82 W ")
#MOBO INTEL
    elif 'tolong rekomendasikan mobo intel' in text_lwr_diterima:
        await update.message.reply_text("Untuk MOBO INTEL (LGA1700) saya dapat merekomendasikan MSI PRO B760M-A WIFI DDR4 MOBO ini dibuat oleh MSI dan MOBO ini adalah bentuk keseimbangan antara harga dengan kinerja untuk sebuah Mother Board yang di bandrol dengan harga 2 jutaan | form factor M-ATX |  4 socket ram (DDR4)  | 4 SATA 6 |2x M.2| 2 USB  3.2 Gen2 (2 Rear) |7 USB  3.2 Gen1 (2 Rear, 4 Front, 1 Rear Type-C) | 6 USB 2.0 (2 Rear, 4 Front)")
#MOBO AMD AM4
    elif 'tolong rekomendasikan mobo amd am4' in text_lwr_diterima:
        await update.message.reply_text("Untuk MOBO INTEL (AM4) saya dapat merekomendasikan MSI B550M Pro-VDH Wifi MOBO ini dibuat oleh MSI dan MOBO ini adalah bentuk keseimbangan antara harga dengan kinerja untuk sebuah Mother Board yang di bandrol dengan harga 2 jutaan | form factor M-ATX |  4 socket ram (DDR4)  | 4 SATA 3 |2x M.2|7 USB  3.2 Gen1 (4 Rear, 2 Front, 1 Front Type-C) | 6 USB 2.0 (2 Rear, 4 Front)")
#MOBO AMD AM5
    elif 'tolong rekomendasikan mobo amd am5' in text_lwr_diterima:
        await update.message.reply_text("Untuk MOBO INTEL (AM5) saya dapat merekomendasikan MSI MAG B650M Mortar WIFI MOBO ini dibuat oleh MSI dan MOBO ini adalah bentuk keseimbangan antara harga dengan kinerja untuk sebuah Mother Board yang di bandrol dengan harga 3 jutaan | form factor M-ATX |  4 socket ram (DDR5)  | 6 SATA 6G |2x M.2| 5 USB 3.2 Gen2 (3 Rear, 1 Front Type-C, 1 Rear Type-C)| 6 USB  3.2 Gen1 (4 Rear, 2 Front) | 4 USB 2.0 (4 Front)")
    elif 'siapa kamu?' in text_lwr_diterima:
        await update.message.reply_text(f"aku adalah {user_bot} yang di buat oleh OKTVK")
    else:
        await update.message.reply_text("bot tidak mengerti. Silahkan gunakan /help untuk mengetahui command list")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Nice picture")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
