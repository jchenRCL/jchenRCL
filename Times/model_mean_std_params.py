# this function is to more easily show the model parameters testing results

def print_results(results):
    print('BEST PARAMS:{}\n'.format(results.best_param_))
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std*2, 3), params))
        
