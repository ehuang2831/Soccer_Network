def run_and_plot_TSNE(X_df = None, Y_df = None, label_map = None, plot_fname = None, title_str = None):

    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=1000)
    tsne_results = tsne.fit_transform(X_df)

    outcomes = list(set(Y_df))

    color=iter(cm.rainbow(np.linspace(0,1,len(outcomes))))

    for i, outcome in enumerate(outcomes):

        subset_indx = (Y_df == outcome)

        vis_x = tsne_results[subset_indx, 0]
        vis_y = tsne_results[subset_indx, 1]
    
        plt.scatter(vis_x, vis_y, c=next(color), label = label_map[outcome])

    plt.legend()
    plt.title(title_str)
    plt.savefig(plot_fname)
    plt.close()

