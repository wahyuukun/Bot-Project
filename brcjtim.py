from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fungsi untuk command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Saya bot pengingat tugas dan event. Gunakan /help untuk melihat daftar perintah.")

# Fungsi untuk command /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Daftar perintah:\n"
        "/start - Memulai bot\n"
        "/help - Mendapatkan bantuan\n"
        "/setreminder [tugas/event] - Mengatur pengingat\n"
        "/listreminders - Menampilkan daftar pengingat\n"
        "/clearreminder [ID] - Menghapus pengingat tertentu"
    )

# Fungsi untuk command /setreminder
async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        reminder = ' '.join(context.args)
        # Simpan pengingat di suatu tempat (misalnya, database atau file)
        await update.message.reply_text(f"Pengingat telah diset: {reminder}")
    else:
        await update.message.reply_text("Tolong masukkan tugas atau event yang ingin diingatkan. Contoh: /setreminder Belanja bahan")

# Fungsi untuk command /listreminders
async def list_reminders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Misalnya, kita ambil pengingat dari suatu sumber data (database/file)
    reminders = ["Belanja bahan", "Meeting dengan klien", "Update konten sosial media"]  # Contoh pengingat
    if reminders:
        await update.message.reply_text("\n".join(reminders))
    else:
        await update.message.reply_text("Tidak ada pengingat yang diset.")

# Fungsi untuk command /clearreminder
async def clear_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        reminder_id = context.args[0]
        # Hapus pengingat berdasarkan ID (misalnya, dari database/file)
        await update.message.reply_text(f"Pengingat dengan ID {reminder_id} telah dihapus.")
    else:
        await update.message.reply_text("Tolong masukkan ID pengingat yang ingin dihapus. Contoh: /clearreminder 1")

# Fungsi utama
def main():
    # Masukkan Bot Token dari BotFather
    TOKEN = "7868862010:AAEdwuVJelq7PZcjRkiSpGK5q-YbWUob7Ws"  # Gantilah dengan token bot Anda

    # Inisialisasi application
    application = Application.builder().token(TOKEN).build()

    # Tambahkan command handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("setreminder", set_reminder))
    application.add_handler(CommandHandler("listreminders", list_reminders))
    application.add_handler(CommandHandler("clearreminder", clear_reminder))

    # Jalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()