from IPython.display import Latex
import matplotlib.pyplot as plt

def lin_rec(m, b, *args):
    """
    List of y values.
    """
    y = []
    for i in args:
        y_i = m*i + b
        y.append(y_i)
    return y


def print_lin_rec(var_str, y_list):
    """
    Prints the values passed as y_list.
    """
    msg = '\nValue(s) corresponding to ' + str(var_str) + ':\n'
    msg += str(var_str) + ' = '
    print(msg, y_list)

    
def plt_lin_rec(xlim_min, xlim_max, ylim_min, ylim_max, x, y, m=1, b=0):
    """
    Plots a single line.
    """
    # Get second line
    x_0 = min(x)-5
    x_n = max(x)+5
    x2 = [x_0, *x.copy(), x_n]
    y2 = lin_rec(m, b, *x2)
    
    # Plot first and second line
    plt.plot(x, y, 'o-', c='blue', linewidth=2)
    plt.plot(x2, y2, c='blue', linewidth=2)
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])
    plt.ylabel('Axis y')
    plt.xlabel('Axis x')
    plt.axvline(x=0, c='black')
    plt.axhline(y=0, c='black')
    plt.show()
    
    
def plt_2lin_rec(rezf, xlim_min, xlim_max, ylim_min, ylim_max, x, y_1, y_2, lbl_1=None, lbl_2=None, intrx=0, intry=0):
    """
    Plots two lines.
    """
    plt.plot(x, y_1, 'o-', c='blue', linewidth=2, label = lbl_1)
    plt.plot(x, y_2, 'o-', c='red', linewidth=2, label = lbl_2)
    plt.xlim([xlim_min-(rezf*xlim_min), xlim_max+(rezf*xlim_max)])
    plt.ylim([ylim_min-(rezf*ylim_min), ylim_max+(rezf*ylim_max)])
    plt.ylabel('Axis y')
    plt.xlabel('Axis x')
    plt.axvline(x=intrx, dashes=[2, 2], c='black')
    plt.axhline(y=intry, dashes=[2, 2], c='black')
    plt.legend()
    plt.show()
    