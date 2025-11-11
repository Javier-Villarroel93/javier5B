from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'mensaje': '¡Hola desde el contenedor Docker!',
        'autor': 'Javier',
        'version': '1.0.1',
        'estado': 'Taller DevOps - Funcionando correctamente'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
