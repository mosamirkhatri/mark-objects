from flask import Blueprint, request, send_file
import os
import xml.etree.ElementTree as ET
import csv
import cv2
import numpy as np

from app.utils.helpers import query_database
from app.db.queries import Query

api = Blueprint('api', __name__)


@api.route('/mark', methods=['POST'])
def mark():
    if request.method == "POST":
        image = request.files['image']
        xml = request.files.get('xml')
        nparr = np.fromstring(image.stream.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        result_img = img
        font = cv2.FONT_HERSHEY_SIMPLEX
        tree = ET.parse(xml)
        root = tree.getroot()
        filename = root.find('filename').text

        for child in root.findall('./object'):
            name = child.find('name').text
            bndbox = child.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            result_img = cv2.rectangle(
                result_img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            cv2.putText(img, name, (xmin, ymin-5), font,
                        1, (0, 0, 255), 2, cv2.LINE_AA)
            query_database(Query.INSERT_OBJECTS, (filename, name,
                           xmin, ymin, xmax, ymax))

        cv2.imwrite('new.jpg', result_img)

        from app import app
        fileToSend = os.path.join(
            os.path.dirname(app.root_path), 'new.jpg')

        return send_file(fileToSend, mimetype="image/jpg", attachment_filename=f"{filename.split('.')[0]}_with_box.jpg", as_attachment=True), 200


@api.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    toCSV = query_database(Query.SELECT_OBJECTS, (start_date, end_date))
    print(toCSV)

    keys = toCSV[0].keys()

    with open('report.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

    from app import app
    fileToSend = os.path.join(
        os.path.dirname(app.root_path), 'report.csv')

    return send_file(fileToSend, mimetype="text/csv", attachment_filename="report.csv", as_attachment=True), 200
