from flask import Flask, send_from_directory, render_template, request

from plugins.mercado_livre import SearcherMercadoLivre
from plugins.amazon import SearcherAmazon

app = Flask(__name__)

@app.route('/<path:path>')
def index(path):
    return send_from_directory('static', path)

@app.route('/list_products')
def list_products():
    search = request.args.get('search')

    try:
        data = []

        try :
            data += (SearcherMercadoLivre()).set_search_term(search).search()
        except:
            pass
        
        try :
            data += (SearcherAmazon()).set_search_term(search).search()
        except:
            pass

        return render_template('list_products.html', data=data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()