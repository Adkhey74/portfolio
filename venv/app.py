from flask import Flask,render_template,send_file

app = Flask(__name__)

@app.route('/')
def home():
    # Votre logique de traitement peut être ajoutée ici
    # Par exemple, rendre un modèle avec render_template
    return render_template('home.html',active_page='Home')


@app.route('/projet.html')
def projet():
    return render_template('projet.html', active_page='Projet')

@app.route('/cv.html')
def cv():
    return render_template('cv.html', active_page='CV')

@app.route('/contact.html')
def contact():
    return render_template('contact.html', active_page='Contact')


@app.route('/download_pdf')
def download_pdf():
    pdf_path = 'static/media/CV.pdf'  # Remplacez cela par le chemin réel de votre fichier PDF
    return send_file(pdf_path, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
