from flask import Flask, send_from_directory, render_template, request

from selenium import webdriver

from plugins.mercado_livre import SearcherMercadoLivre
from plugins.amazon import SearcherAmazon

from models.products import Product

app = Flask(__name__)

@app.route('/<path:path>')
def index(path):
    return send_from_directory('static', path)

@app.route('/list_products')
def list_products():
    search = request.args.get('search')

    driver = webdriver.Chrome()
    try:
        ((SearcherMercadoLivre()).set_search_term(search).search(driver=driver).save())
        ((SearcherAmazon()).set_search_term(search).search(driver=driver).save())
    except Exception as e:
        return str(e)
    finally:
        driver.quit()

    data = (Product.select()
            .where(Product.term == search)
            .group_by(Product.link)
            .order_by(Product.score.desc())
            .dicts())

    return render_template('list_products.html', data=data)

if __name__ == '__main__':
    app.run(port=2000)