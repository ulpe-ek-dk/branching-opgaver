@app.route("/api/devices", methods=["GET"])
def get_devices():
    """
    Vis alle registrerede IoT enheder - test - test - test
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, location, status, customer_name, last_seen FROM devices")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/api/devices3", methods=["GET"])
def get_devices():
    """
    Vis 3 vindmøller - test - test
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, location, status, customer_name, last_seen FROM devices")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)
