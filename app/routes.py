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

        # Initalize graph data
        graph = Graph(vertices)

        # Parse edges from form data
        for edge in edge_data:
           u, v, w = map(int, edge.split(','))
           graph.add_edge(u, v, w)

        # Run Bellman-Ford algorithm
        result = graph.bellman_ford(source_vertices)

        # Return result
        if isinstance(result, str):
           return render_template('index.html', error=result)
        else:
           dist, predecessor = result
           path_list = graph.get_path(predecessor, destination)
           path = graph.construct_path(path_list, source_vertices, destination)
           path = {'source': source_vertices, 'destination': destination, 'path': path}
           return render_template('result.html', dist=dist, predecessor=path_list, path=path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('start.html')
    if request.method == 'POST':
        num_vertices = int(request.form['vertices'])
        num_edges = int(request.form['edges'])

        return redirect(url_for('indexs', vertices=num_vertices, edges=num_edges)) 
        # return render_template('start.html')

