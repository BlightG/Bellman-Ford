from flask import request, render_template, redirect, url_for, flash
from app import app
from graph.belman import Graph
from app.utils.combinations import combinations

@app.route('/edges', methods=['GET', 'POST'])
def indexs():
    vertices = request.args.get('vertices')
    edges = request.args.get('edges')

    if vertices is None or edges is None:
        return redirect(url_for('index'))

    vertices = int(vertices)
    edges = int(edges)
    max_edge = combinations(vertices)

    if request.method == 'GET':
        if max_edge < edges:
            edges = max_edge
            flash(f"with {vertices} verticees maximun allowd edges is {max_edge} ")
        return render_template('/index.html', vertices=vertices, edges=edges)

    if request.method == 'POST':
        source_vertices = int(request.form['source'])
        destination = int(request.form['destination'])
        edge_data = request.form.getlist('edges[]')
        max_stops = int(request.form['max_stops'])
        # Initalize graph data
        graph = Graph(vertices)

        # Parse edges from form data
        for edge in edge_data:
            try:
                u, v, w = map(int, edge.split(','))
                graph.add_edge(u, v, w)
            except(ValueError) as result:
                return render_template('error.html', error=result)


        # Run Bellman-Ford algorithm
        result = graph.bellman_ford(source_vertices)

        if result == -1:
            return render_template('error.html', error="Negative cycle detected")
        
        # Return result

        dist = result
        path_list = graph.get_path(destination, max_stops)
        if path_list == -1:
            return render_template('error.html', error="No path Found")
        path = graph.construct_path(destination)
        path = {'source': source_vertices, 'destination': destination, 'path': path}
        return render_template('result.html', dist=dist[max_stops], predecessor=path_list, path=path)
        

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('start.html')
    if request.method == 'POST':
        num_vertices = int(request.form['vertices'])
        num_edges = int(request.form['edges'])

        return redirect(url_for('indexs', vertices=num_vertices, edges=num_edges)) 
        # return render_template('start.html')

