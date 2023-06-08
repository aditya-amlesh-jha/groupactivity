# creating a route to delete data from the database using a form
    # @app.route('/delete',methods=['GET','POST'])
    # def delete():
    #     if request.method == 'POST':
    #         id = request.form['id']
    #         mydb.deleteData(table_name,id)
    #         return redirect(url_for('index'))
    #     return render_template("delete.html")