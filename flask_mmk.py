
from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from werkzeug.exceptions import abort

model = SentenceTransformer('distiluse-base-multilingual-cased')


app = Flask(__name__)


@app.route('/api/text', methods=['POST'])
def api_text():
    if not request.form or not 'sent_1' in request.form or not 'sent_2' in request.form:
        abort(400)
    sent_1 = request.form['sent_1']
    sent_2 = request.form['sent_2']  
    sentence_embeddings_sent_1 = model.encode(sent_1).reshape(1,512)
    sentence_embeddings_sent_2 = model.encode(sent_2).reshape(1,512)
    if cosine_similarity(sentence_embeddings_sent_1,sentence_embeddings_sent_2) > 0.5:
        text = 'These sentences are similar'
    else:
        text = 'These sentences are not similar'

    return jsonify(text)


if __name__== '__main__':
    app.run('0.0.0.0',8000, debug = True)

