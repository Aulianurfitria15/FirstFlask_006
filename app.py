from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data dari form menggunakan request.form
    nama_pria = request.form.get('nama_pria')  # Nama calon mempelai pria
    nama_wanita = request.form.get('nama_wanita')  # Nama calon mempelai wanita
    umur_pria = request.form.get('umur_pria')  # Umur calon mempelai pria
    umur_wanita = request.form.get('umur_wanita')  # Umur calon mempelai wanita
    tanggal_nikah = request.form.get('tanggal_nikah')  # Tanggal rencana pernikahan
    alamat_pria = request.form.get('alamat_pria')  # Alamat calon mempelai pria
    alamat_wanita = request.form.get('alamat_wanita')  # Alamat calon mempelai wanita
    wali_nikah = request.form.get('wali_nikah')  # Nama wali nikah

    return render_template(
        'result.html', 
        nama_pria=nama_pria, 
        nama_wanita=nama_wanita, 
        umur_pria=umur_pria, 
        umur_wanita=umur_wanita, 
        tanggal_nikah=tanggal_nikah, 
        alamat_pria=alamat_pria, 
        alamat_wanita=alamat_wanita, 
        wali_nikah=wali_nikah)

if __name__ == '_main_':
    app.run(debug=True)