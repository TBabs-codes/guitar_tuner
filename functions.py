

harmonics = {'E': [82.41, 164.82, 247.23, 329.64, 412.05], 
             'A': [110, 220, 330, 440, 550], 
             'D': [146.83, 293.66, 440.49, 587.32, 734.15], 
             'G': [196, 392, 588, 784, 980], 
             'B': [246.94, 493.88, 740.82, 987.76, 1234.7], 
             'High E': [329.63, 659.26, 988.89, 1318.52, 1648.15]}

def guess_string(fundamental_frequency):
    
    if 70 <= fundamental_frequency < 100:
        return "E string"
    elif 100 <= fundamental_frequency < 130:
        return "A string"
    elif 130 <= fundamental_frequency < 175:
        return "D string"
    elif 175 <= fundamental_frequency < 225:
        return "G string"
    elif 225 <= fundamental_frequency < 280:
        return "B string"
    elif 280 <= fundamental_frequency < 360:
        return "HIGH E string"


def find_fundamental_freq(x, y):
    
    first_peak_found = False
    sum_freq = 0
    sum_power = 0

    for i, power in enumerate(y):

        if power >= 0.18:
            first_peak_found = True

            sum_freq += x[i] * power
            sum_power += power

        if first_peak_found and power < 0.1:
            break

    if sum_power!= 0:
        return sum_freq/sum_power
    
    

def find_prom_freqs(x, y):
    freqs = []
    
    peak_found = False
    sum_freq = 0
    sum_power = 0

    for i, power in enumerate(y):

        if not peak_found and power >= 0.18:
            peak_found = True
            for j, i_power in enumerate(y[:i][::-1]):
                if i_power > 0.05:
                    sum_freq+= x[i-1-j] * i_power
                    sum_power+= i_power
                else:
                    break

        if peak_found and power >= 0.03:

            sum_freq += x[i] * power
            sum_power += power

        if peak_found and power < 0.03:
            peak_found = False
            freqs.append(sum_freq/sum_power)
            sum_freq = 0
            sum_power = 0
    

    
    return freqs