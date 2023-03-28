

def Eucliadian_dist(expected_values, session_letters, n_session):
    result = []
    for i in expected_values:
        dist_eucliadian = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[n_session][j]['Key']:
                dist_eucliadian += pow(float(i[j]['Value']) - session_letters[n_session][j]['Value'], 2)
                k = pow(dist_eucliadian, 0.5)
        result.append(k)
    return result