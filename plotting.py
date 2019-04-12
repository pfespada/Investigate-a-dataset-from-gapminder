def plot_variable(data_frame,countries, variable,title):
    
    plt.figure(figsize=(20,20))
    
    for e in countries:
        plt.plot(data_frame[data_frame['Country']== e]['Year'],data_frame[data_frame['Country']== e][variable])
        
    plt.legend(countries)
    plt.title(title, fontsize=20)
    plt.xlabel('YEAR', fontsize=14)
    plt.ylabel('USD', fontsize=14)
