
def get_process_data_for_zkp(id):

    csv_paths = parser.get_csv_paths()
    csv_path = csv_paths[0]

    df_high_quality = filter_bpmn_models(csv_path)
    graph = json_to_labeled_graph(df_high_quality.iloc[id]['Model JSON'])
    node_data = graph.nodes.data()
    edge_data = graph.edges.data()
    G_1 = json_to_detailed_graph(df_high_quality.iloc[id]['Model JSON'])

    #print('G_1',G_1.nodes.data())
    #print('G_1',G_1.edges.data())

    node_data_csv = []
    edge_data_csv = []

    id  = []
    label = []
    task_type = []
    original_name = []

    n_data = G_1.nodes.data()

    for d in n_data:
        if len(d[1])>0:
            id.append(d[0])
            label.append(d[1]['label'])
            task_type.append(d[1]['task_type'])
            original_name.append(d[1]['original_name'])
        else:
            id.append('')
            label.append('')
            task_type.append('')
            original_name.append('')
            
    node_data = {"id":id,"label":label,"task_type":task_type,"original_name":original_name}
    node_df = pd.DataFrame(node_data)
    #print('node df',node_df)

    edge_data = graph.edges.data()
    #print('edge_data',edge_data)
    from_node = []
    to_node = []
    label = []
    for edge in edge_data:
        from_node.append(edge[0])
        to_node.append(edge[1])
        if len(edge[2]['label'])>0:
            label.append(edge[2]['label'])
        else:
            label.append('')

    edge_data = {"from_node":from_node,"to_node":to_node,"label":label}
    edge_df = pd.DataFrame(edge_data)
    #print('edge_df',edge_df)

    return(node_df,edge_df)


