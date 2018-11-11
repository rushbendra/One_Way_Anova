{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYwAAAEKCAYAAAAB0GKPAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzt3X2c1WP+x/HXR6JSbrYbdKdQSAmN3NvCKoWERSFyk/tlsT/3Su1iRXKTJTfRspVdpVak1CStyJTuS0IYM+n+RlNNzXx+f3zOmGk6M/NtZs75nnPm83w85jFzvud7zvkcjfOe67q+13WJquKcc86VZY+wC3DOOZccPDCcc84F4oHhnHMuEA8M55xzgXhgOOecC8QDwznnXCAeGM455wLxwHDOOReIB4ZzzrlA9gy7gMpUr149bdasWdhlOOdc0pg1a9ZqVa0f5NyYBYaINAGGAwcB+cBQVX1WREYBR0RO2x9Yr6rHRnn8cmATkAfsUNW0sl6zWbNmZGRkVNI7cM651CciPwQ9N5YtjB3A3ao6W0TqALNEZJKqXlZwgog8DWwo5Tk6qurqGNbonHMuoJgFhqpmA9mRnzeJyGKgEbAIQEQEuBQ4M1Y1OOecqzxxGfQWkWbAccAXRQ6fDvyiqt+U8DAFJorILBHpE9sKnXPOlSXmg94iUht4F7hTVTcWuasHMKKUh56qqlki0gCYJCJLVHValOfvA/QBaNq06S5Psn37djIzM9m6dWtF3kZoatSoQePGjalevXrYpTjnqjiJ5X4YIlIdeB/4SFUHFTm+J/Az0E5VMwM8Tz/gV1V9qrTz0tLStPig9/fff0+dOnWoW7cu1guWPFSVNWvWsGnTJpo3bx52Oc65FCQis4JcVAQx7JKKjFG8BiwuGhYRZwNLSgoLEdknMlCOiOwDnAMsKE8dW7duTcqwABAR6tatm7StI+dcaonlGMapwFXAmSIyJ/LVJXLf5RTrjhKRhiLyQeTmgcB0EZkLzATGq+qE8haSjGFRIJlrd86lllheJTUdiPppp6rXRDmWBXSJ/Pwd0DZWtTnnnNt9vjSIc865QDwwnHPOBeKBEcXmzZvp2rUrbdu2pXXr1owaNYpmzZqxerVNOs/IyKBDhw4A9OvXj6uuuoozzzyTFi1a8MorrwAwdepUzjjjDLp3706rVq246aabyM/PD+stOeeSQXo6NGtm3xOQB0YUEyZMoGHDhsydO5cFCxbQuXPnUs+fN28e48ePZ8aMGfTv35+srCwAZs6cydNPP838+fP59ttvGT16dDzKd84lo/R0srtez+9/eJMVXa9LyNDwwIiiTZs2fPzxx9x77718+umn7LfffqWe361bN2rWrEm9evXo2LEjM2fOBKB9+/YceuihVKtWjR49ejB9+vR4lO+cSzbp6XDeeQzYcjfTOY0BW+6G885LuNDwwIiiZcuWzJo1izZt2nD//ffTv39/9txzz9+6lIrPiyh+6WvB7ZKOO+fcbyJhkZ2zL8PoTT7VGEZvVuTUSbjQ8MCIIisri1q1anHllVdyzz33MHv2bJo1a8asWbMAePfdd3c6f+zYsWzdupU1a9YwdepUTjjhBMC6pL7//nvy8/MZNWoUp512Wtzfi3MugUXCgpwcBvAw+ZGZCHnswQAehpychAoND4wo5s+fT/v27Tn22GP529/+xkMPPUTfvn254447OP3006lWrdpO57dv356uXbty0kkn8fDDD9OwYUMATj75ZO677z5at25N8+bN6d69exhvxzmXiIqERTYHMYze5FIDgFxqWCuDAxMqNFJqx73K0qlTJzp16rTL8aVLl0Y9v2XLlgwdOnSX47Vq1WLUqFGVXp9zLskVCQuAR3mE7cU+jgtaGUO4rTA03n8fOnYMo2LAWxjOORdfGzdCjx6Qk8MOqvEctzGUG8lj5xWpd2plgIVG794hFFzIWxgV1K9fv6jHO3To8NtcDedcFZSXB99+C/Pm2dfcufZ9+XLy2IMRXEF/HuEbWmK7WEd5iqKtjFq1YNiw+L6HYjwwnHOuotauhfnzdw6GBQtgyxa7f4894IgjyDvhJEaeMJj+n53F0p9r04pF7MU2ctk76tMWtDIervk0B73/WqjdUeCBEV16ujX9hg0L/R/IOZdAduyAr78ubDUUfGUW2amhbl1o2xZuvNG+H3MMeS2PYtS4mvTvbw9v0wbefQ4mvbEfy/5b+p5EeezBgHOmMaRj4xi/ubJ5YBRXdDAqAQaZnHMhWbly12BYuBByc+3+PfeEo46CDh3gmGMKvw46CCJzrvLy4N//hv5XwuLF0Lo1/Oc/0L27NToGDGhEbhll5FKDz34IPyzAA2Nnxa5c8NBwrgrYtg2WLNk5GObOhV9+KTznoIOstXD22YXBcOSRsNdeUZ8yPz8SFP1h0SI4+mh45x24+GILigJffRX5ofhnD9iYRYJ99nhgFIj2DwaVEhqZmZnceuutLFq0iPz8fM477zwGDhzIZ599xlNPPcX7779fCW/AOVcqVcjO3jUYliyxriaAvfe2T/dzzy0MhjZtoEGDQC+Rnw/vvguPPmqNkVatYNQouOSSnYNiFx072mdMwWdQAoYFxDAwRKQJMBw4CLsEYKiqPhvZn/sGYFXk1AdU9YMoj+8MPAtUA15V1SdiVWuJYVGgAqGhqlx00UXcfPPNjB07lry8PPr06cODDz5I165dK6F459wutmyxP+2LDkLPmwdr1hSe06SJBcL55xeGQ8uW1tW0m/LzYfRoC4oFC6ynauRIC4pi83xLVhAaCTx+GssWxg7gblWdHdmfe5aITIrc94yqPlXSA0WkGjAE+AOQCXwpIuNUdVGlV1lWWBQoZ2hMmTKFGjVq0Dty/XS1atV45plnaN68OR0T8BfCuaSiCj/9tGswLF1qn+Jgf623bm0DB5FBaNq0gQMOqPDL5+fDmDEWFPPnWy/Vv/4Fl166G0FRVMeOsHx5heuKlVhu0ZoNZEd+3iQii4FGAR/eHlgW2aoVERkJdAMqFhh33glz5hTeXrfO/hwIuk9FTo71YbZuXfjLduyxMHhwiQ9ZuHAh7dq12+nYvvvuS9OmTVm2bNnuvgPnqq5ff7X/X4sPRG/YUHhO8+YWCJdeWthqOPTQcn56lyw/H8aOhX79rIQjjoC334bLLqv0l0oocRnDEJFmwHHAF8CpwG0i0gvIwFoh64o9pBHwU5HbmcCJlV7Y118HD4sC+fn2uJNOCnS6qkZdpbak485Vefn58P33uwbDt99aiwKgTh0Lg549C4OhdWvYd9+YlqZqQfHoo/a3Z8uW8NZbcPnlqR0UBWIeGCJSG3gXuFNVN4rIP4ABgEa+Pw1cW/xhUZ4q6sXKItIH6APQtGnT0osp3hII2h1V1G4ORh199NG7rG67ceNGfvrpJw477LDgr+tcKtqwoXDCW0G30vz5sHmz3S8CLVpYS75Xr8JwOOSQMkaRK5cqjBtnLYo5c+Dww2H4cFvhoxxDHkkrpm9VRKpjYfG2qo4GUNVfitz/ChDtEqFMoEmR242BrGivoapDgaEAaWlppc+AKa74lQllKceVC2eddRb33Xcfw4cPp1evXuTl5XH33XdzzTXXUKtWrd0q17mklZcHy5btukzGDz8UnnPAARYG115r39u2tcuM9tkntLJV7X/5fv1g9mwLijfftIZNVQqKArG8SkqA14DFqjqoyPGDI+MbAN2BBVEe/iXQQkSaAz8DlwM9Y1Jo0NAo52VuIsKYMWO45ZZbGDBgAPn5+XTp0oXHHnuMTz/9lL33jr4kgHNJa80aayUUHYResAAKNh6rVs06/U8+eafZ0DRq9NuEt7CpwvjxFhSzZsFhh8Ebb8AVV1TNoCgQy7d+KnAVMF9ECkaaHwB6iMixWBfTcuBGABFpiF0+20VVd4jIbcBH2GW1r6vqwphVWlZoVPCa6CZNmvDf//53l+MLFy70bimXvLZvj75Mxs8/F55Tv74Fwi23FHYnHXUU1KgRXt2lUIUPPrCgyMiwMfTXX4crr4Tq1ct8eMqL5VVS04k+FrHLnIvI+VlAlyK3Pyjp3JgoKTRiNIHmuuuuY8GCBbzzzjuV+rzOxcQvv+waDIsWFS6TUb26dR+deebOy2QceGDCtBpKowoTJlhQzJxpQfHaa3DVVR4URVXhxlUUcZxt+dprr1X6czpXYdu22aJHxWdDr1xZeE7DhhYG55xTGAxHHFHiMhmJTBU++siC4osvoFkzePVVG1/3oNiVB0ZxSTDb0rkKU4WsrF0HoZcssQFqsGUyWreGrl13bjXUqxdu7ZVAFSZOtKD4/HNo2hSGDoWrr07K3IsbD4xoEny2pXO7JScn+jIZa9cWntO0qYVBt26Fg9CHH55yI7yq8PHH0LcvzJhhb/vll+Gaazwogkit3wbnqjJVu0y1+FjDN9/svExGmza2yFHRxfX23z/c2mNMFSZPthbF//5ny0i99JJ1JHhQBOeBEUV2ts3cHDXKVjV2LuFs2hR9mYyNGwvPOewwC4TLL995mYw4TngLmypMmWJBMX06NG4ML75oUz38ivbd54ERxYAB9ss1YAAMGVKx5+rQoQP3338/nTp1+u3Y4MGDWbp0KXfeeSd33nknS5cupXr16rRp04bnn3+eAw88sILvwKWM/Hz47rtdB6G/+67wnH33tTC48sqdl8moUye8uhNAerp1PX36qU3xeOEFuP56D4qK8MAoJjvbxrrz8+37ww9XrJXRo0cPRo4cuVNgjBw5koEDB9K1a1cGDRrE+eefD0B6ejqrVq3ywKiq1q/fdZmMBQsKl8nYYw9bJqNdO+tLKZgN3bRpUly6Gi9Tp1qL4pNP7IKu55+3oEjQqR9JxQOjmAEDCrt78/Iq3sq45JJLeOihh9i2bRt77703y5cvJysri6VLl3LyySf/FhaAL3deVezYUbhMRtFB6B9/LDznd7+zQLjuusJB6FatbAzCRTVtmrUopk6Fgw+G556DG27woKhMVSowiq9uXty2bTZppyAwcnNtYOyrr0oeGCtjdXPq1q1L+/btmTBhAt26dWPkyJFcdtllUZc9dylo9ero+0IXXSbjyCPhtNN2vnS1YUNvNQT06afWopgyxXoDBg+GPn2gZs2wK0s9VSowyvLDD4WrJxcouPCkRYvyP29Bt1RBYLz++uu89dZbFSvWJZbc3OjLZGQVWTOzQQNrLdx6687LZHinerlMn25BMXmyTSh/5hlbmsqDInaqVGCU1hLIzrYLSKIFxrp1tt1ieccyLrzwQu666y5mz57Nli1bOP744/nqq6/45JNPyveELjyqJS+TsX27nbPXXtZ9dPbZuy6T4Srss8+s6+njj+0/6aBBFhTeWxd7VSowSlN07KK4io5l1K5dmw4dOnDttdfSo0cPAHr27Mnjjz/O+PHjf9vbe8KECTRq1Ig2bdqU74VSWXp6/Gffb9268zIZBeMNq1YVntOokYVB586Fg9AtW/q6EjEwY4a1KCZOtMbaU0/BzTd7UMSVqqbMV7t27bS4RYsW7XKsuKws1Ro1VO3Px+hfNWuqZmeX+VQlGj16tAK6ePHi344tXrxYO3XqpIcffrgeddRRetlll+mKFSvK9R5S2pQpqrVq2T9ErVp2uzLl56v+9JPq+PGqjz+uevnlqq1aqVarVvgLUKOGalqa6rXXqj77rGp6uurq1ZVbh4tqxgzVTp3sn6F+fdWBA1V//TXsqlIHkKEBP2O9hUHprYsCFW1ldO/eHS3W33XkkUcyYcKE8j1hVVF8V8ScHLtd3kUhc3KiT3hbV2SX4EMOsdbCRRcVdicdfnjV2IMzgcycaV1PEybY8lVPPmmrpIe4n1KV54GBNXULVmkuSW6u9Z26OCppC90goaFq64FFWyajILj32cfC4NJLd14mY7/9Yvq2XOm+/NK6nj74AOrWhSeesOsEatcOuzLngYFdNusSTFn7rRcNjbS0nSe8FXxt2mTnihQuk9GzZ2E4NG9epZbJSHQZGRYU48fbNJTHH4fbbvOgSCSx3KK1CTAcOAjIB4aq6rMiMhA4H8gFvgV6q+r6KI9fDmwC8oAdqppW3lpUFUnSa9qLd2NVCWWFRYGcHDjrrJ0vbdtvPwuDXr0KB6GPPto/dRLYrFkWFO+/b0Hx2GMWFFV8ZZOEFMsWxg7gblWdLSJ1gFkiMgmYBNyvtg3r34H7gXtLeI6Oqrq6IkXUqFGDNWvWULdu3aQLDVVlzZo11KhKU1WDhkUBVbsiqV8/W0upSROf8JYkZs+GRx+FcePggAPgr3+F22+3pbFcYorlFq3ZQHbk500ishhopKoTi5z2OXBJrGoAaNy4MZmZmawqeilkEqlRowaNGzcOu4z46d07eFgU2L7ddr954IHY1OQq1Zw5lu9jx9qq6gMGwJ/+5EGRDOIyhiEizYDjgC+K3XUtMKqEhykwUUQUeFlVh5bntatXr07z5s3L81AXhmHDdq+FAXYh/rBhsavJVYq5cy0o3nvPeg4ffRTuuMOvMUgmMR/xE5HawLvAnaq6scjxB7Fuq7dLeOipqno8cC5wq4icUcLz9xGRDBHJSNZWhCuiYIvcoLOxYrjvuqsc8+bBxRfbumvp6RYay5fDI494WCSbmAaGiFTHwuJtVR1d5PjVwHnAFVrCqK6qZkW+rwTGAO1LOG+oqqapalr9+vUr+y24MHTsCP37l32eh0VCmz/fNvZr27ZwW9Tly+17im/wl7JiFhhiI8yvAYtVdVCR452xQe4LVDVqv4OI7BMZKEdE9gHOARbEqlaXYD75xP78bNas5JXkPCwS1oIF8Mc/2kVqEyfanjLLl1vLwoMiucWyhXEqcBVwpojMiXx1AV4A6gCTIsdeAhCRhiLyQeSxBwLTRWQuMBMYr6o+JboqmD4duna12daff24X5RfvnvKwSEgLF8Jll1lQfPQRPPSQBUX//nYVlEt+kkrX+aelpWlGRkbYZbjymjEDzjnHFvSbOrVweeCil9p6WCScRYssFN55xybP33EH3HWXzalwiU9EZgWd5+bTXF1i+OIL6NTJtkor2AmnQMFA+CGHeFgkkMWLbeJ869bWELzvPmtR/PWvHhapypcGceHLyLCwqF/fwqJhw13P6djRPo1c6JYssbkTI0ZYg+/ee+Huu22BQJfaPDBcuGbPhj/8wTq509OhKk1STDJLl1rX04gRdi3C//0f3HOPB0VV4oHhwjN3roXFvvtaWDRtGnZFLoqlS62b6e23oUYNa0385S/WIHRViweGC8f8+bZwYK1aFhbNmoVdkSvmm28sKN56y7Ydv+suC4oGDcKuzIXFA8PF36JFFhZ7721hceihYVfkivj2WxujeOst2578z3+2oPAtyZ0HhouvJUvgzDNt97r0dNvJziWE776zFsXw4bYA8J/+ZOMURS9Yc1WbB4aLn6VLLSzAwqJly3DrcQB8/70FxZtvWlDcfrtd+eRB4YrzwHDxsWyZXRq7Y4eFxZFHhl1RlVcwZ+LNN63Bd9ttFhQHHxx2ZS5ReWC42PvuOwuLbdssLI4+OuyKqrTly21Xu2HDLChuvtkm3UWb/uJcUR4YLraWL7ewyMmxSXlt2oRdUZX1ww+FQSECN91kQdGoUdiVuWThgeFi58cfbcxi40aYPNnWuXZx9+OPFhSvv25BccMNcP/9PkfS7T4PDBcbmZkWFmvX2mYIxx8fdkVVzk8/weOPw6uv2u3rr7egaNIk3Lpc8vLAcJUvK8vCYuVKmDQJ0gIthOkqSWZmYVCownXXWVD4RHpXUR4YrnKtWGFhkZ1tmyKceGLYFVUZP/8MTzwBQ4dCfj5cey088IAt8utcZfDAcJVn5UoLi8xMmDABTjkl7IqqhKyswqDIy4PevS0ofLUVV9liuUVrExFJF5HFIrJQRO6IHP+diEwSkW8i36PuxSUiV0fO+SayB7hLZKtW2XIfy5fb5ginnRZ2RSkvO9s2Kzr0UPjHP+Cqq2xu5NChHhYuNmK5gdIO4G5VPQo4CbhVRFoB9wGTVbUFMDlyeyci8jugL3Ai0B7oW1KwuASwZg2cfbZNznv/ffj978OuKKVlZ9v6ToceCkOGwBVXwNdfwyuvQPPmYVfnUlnMAkNVs1V1duTnTcBioBHQDXgzctqbwIVRHt4JmKSqa1V1HTAJ6ByrWl0FrF1rYfH11zBuXOHSH67SrVhhK8Yeeig8/zz06GH/2V97zddvdPERlzEMEWkGHAd8ARyoqtlgoSIi0RZLbgT8VOR2ZuSYSyTr19se3IsWwdixtreFq3S//AJPPmndTrm51vX04IO+bqOLv5gHhojUBt4F7lTVjSIS6GFRjmkJz98H6APQ1K8bjJ8NG2xb1XnzYMwY6OwNwMq2ciUMHGjdTtu2wZVXwsMPe1C48JQZGCJSH7gBaFb0fFW9NsBjq2Nh8baqjo4c/kVEDo60Lg4GVkZ5aCbQocjtxsDUaK+hqkOBoQBpaWlRQ8VVsk2b4NxzbXvV//wHunYNu6KUsmpVYVBs3WpjFA895Iv7uvAFaWGMBT4FPgbygj6xWFPiNWCxqg4qctc44Grgicj3sVEe/hHwWJGB7nOA+4O+touhX3+FLl1g5kx45x3o1i3silLG6tUWFC+8YEHRs6cFxRFHhF2ZcyZIYNRS1XvL8dynAlcB80VkTuTYA1hQvCMi1wE/An8EEJE04CZVvV5V14rIAODLyOP6q+ractTgKtPmzdaamDEDRoyAiy4Ku6KUsHo1PP20DWTn5Nhg9sMP+wrwLvGIaum9OCLyV+AzVf0gPiWVX1pammZkZIRdRmrKyYHzzoNPPrG9O3v0CLuipLdmTWFQbN4Ml19uQXHUUWFX5qoSEZmlqoHW7wnSwrgDeEBEcoFcbEBaVXXfCtToksmWLdb1NHWq7d/pYVEha9daUDz3nAXFZZdZULRqFXZlzpWuzMBQ1TrxKMQlqK1bretp8mTbSOHKK8OuKGmtWweDBsGzz9pQ0B//CI884vtJueQR5CopAa4AmqvqABFpAhysqjNjXp0L17ZtcMklti7Uq6/C1b5CS3msWwfPPGNBsXFjYVC0bh12Zc7tniAzvV8ETgZ6Rm7/CgyJWUUuMeTmwqWX2rpQL79sa2S73bJ+PfTta+s6DRhg8xrnzbOLyzwsXDIKMoZxoqoeLyJfAajqOhHZK8Z1uTBt324jsOPG2WSAPn3CriipbNgAgwdbq2LDBuvR69sXjjkm7Mqcq5gggbFdRKoRmWkdmciXH9OqXHh27LAJAGPGWB/KLbeEXVHS2LDB/pM984y1Lrp3t66nY48NuzLnKkeQwHgOGAM0EJG/AZcAD8W0KheOHTtsoaL//MdGZ//0p7ArSgobN9oVT4MG2XhFt27WojjuuLArc65yBblK6m0RmQWchV1Se6GqLo55ZS6+8vLgmmtg5Ehb6e7Pfw67ooS3caPNoXj6aQuKCy6woPDty12qKjEwIntSFFgJjCh6n8+8TiF5ebaf59tvw2OPwV/+EnZFCW3TpsKgWLsWzj/fgqJdu7Arcy62SmthzMLGLQpWji2YEi6Rn30F/lSQn2+D2sOHQ//+cL8v2VWSTZvsGoCnnrJZ2l27Qr9+kBZojqxzya/EwFBV37sr1eXnw003weuv2+jsww+HXVFC+vVXC4qBAy0ounSxFkX79mFX5lx8xWUDJZeAVOG222xfzwcesD+V3U42by4MitWrbUX3vn3hxBPDrsy5cHhgVEWqcMcdtoXb//0f/PWvEGxjqyph82b7T/Pkk7Y3RadOlqcnnRR2Zc6Fq8SZ3iLiXVKpSNU2hn7+efv+xBMeFhE5OTaQfeihNu5/3HHw2We2MoqHhXOlLw3yHwARmRynWlysqVqLYvBgm2Px1FMeFlhQDBoEzZvDPfdA27YwfTp89BGcfHLY1TmXOErrktpDRPoCLUXkruJ3FttFzyU6VRureOopm709eHCVD4stW2yZrL//HVasgLPOsq6n004LuzLnElNpgXE5cGHknN1e4lxEXgfOA1aqauvIsVFAwYaT+wPrVXWXhRNEZDmwCdsSdkfQzT1cKfr2te6nG2+07qgqHBZbtsDQofafY8UKOPNMWxDw9NPDrsy5xFbaZbVfA38XkXmq+mE5nvsN4AVgeJHnvKzgZxF5GthQyuM7qurqcryuK65/f1su9brr4MUXYY8gixSnnq1bC4MiOxs6dLCJ7b//fdiVOZccglwl9ZmIDALOiNz+BNtju7QPe1R1mog0i3ZfZI+NS4Ezg5fqyuWxx6x1cc019mlZBcNi61bbzuPxxyErC844A/71LwsM51xwQT49Xse6hy6NfG0EhlXwdU8HflHVb0q4X4GJIjJLRHxt7fJ68kl48EHbJe/VV6tcWGzbZvMoDj8cbr8dDjsMpkyxbck9LJzbfUFaGIep6sVFbj8qInMq+Lo9KLI2VRSnqmqWiDQAJonIElWdFu3ESKD0AWjatGkFy0ohgwbBvffa/ttvvAHVqoVdUdxs22aT1x97DDIzbRB7+HDo2LFKD904V2FB/uTcIiK/XTciIqcCW8r7giKyJ3ARMKqkc1Q1K/J9Jba0eomLMKjqUFVNU9W0+vXrl7es1PLcc3D33bYX6PDhVSYscnPhpZegRQu7EKxpU5g0CaZNs4FtDwvnKiZIYNwEDBGR5ZGrl14AbqzAa54NLFHVzGh3isg+IlKn4GfgHGBBBV6vahkyxGZxd+9uq8/umRqT+bOzbXB6xYpd78vNteGZFi3g5puhcWOYONHmUpx9tgeFc5WlzMBQ1bmq2hY4BjhGVY9T1XllPU5ERgAzgCNEJFNECjaFvpxi3VEi0lBEPojcPBCYLiJzgZnAeFWdEPwtVWEvv2zrQ11wgV3+U7162BVVmgEDLAAGDCg8lptrS2G1bGlXCzdsaJPt/vc/2z/bg8K5yiWqWvZZSSItLU0zMjLCLiMcr70G119va26/+y7svXfYFVWa7GxbrmPrVqhZE77+2oLhb3+D5cttMcB+/WzNJw8J53aPiMwKOtctNforqro33oAbboDOnW171RQKC7BWRX5kF/ncXDj6aNub4oQTbFpJ584eFM7FgwdGsnvrLdst7+yzYfRoqFEj7IoqVXZNAZgYAAAWyElEQVQ2DBtmQQG2OeCvv8I//wlXXOFB4Vw8BQoMETkFaFb0fFUdXuIDXHyMGAFXX23Xi773nvXXpJgBAywkiqpeHWbMsOklzrn4KXPQW0T+CTwFnAacEPnytZ3C9s479ol5+ukwbhzUqhV2RZUuO9uGZrZv3/l4bq61OqJdMeWci50gLYw0oJWm0uh4snv3XejZE045Bd5/H/bZJ+yKYuKaawq7oorLy7PWx5AhcS3JuSotyDyMBcBBsS7EBTR2LFx+uW0o/cEHULt22BXFxODBNpeiJN7KcC7+ggRGPWCRiHwkIuMKvmJdmIvi/fdt9na7drYNXJ3dXnU+KTz/PPz5z2UPaBe0Mpxz8RGkS6pfrItwAXz4IVx8sW0HN2EC7Ltv2BVVOlVb/+mhh2C//WBDqeshWyvjs8/iU5tzLkBgqOon8SjElWLiRFvq4+ij7ef99w+7okqnamslDhwIV11liwemyKomzqWMIFdJnSQiX4rIryKSKyJ5IrIxHsU5YPJk6NYNjjzSVtI74ICwK6p0eXm2BtTAgbZo4BtveFg4l4iCjGG8gC1H/g1QE7g+cszF2tSpcP75tqrexx9D3bphV1Tptm+HXr1sGaz774cXXqhy23Y4lzQC/R2nqstEpJqq5gHDRMR7jmPt009tXajmzS0s6tULu6JKt3UrXHaZTSN5/HG4776wK3LOlSZIYOSIyF7AHBF5EsgGUvPC/0Txv//Buefahg5TpkCDBmFXVOl+/dV62qZMsbkUt9wSdkXOubIEafxfFTnvNmAz0AS4uNRHuPL7/HMLi0aN7NP0wAPDrqjSrVtny49/8omtCeVh4VxyCHKV1A8iUhM4WFUfjUNNVdeXX9oa3Q0aWFgcfHDYFVW6X36Bc86BJUtsYd0LLwy7IudcUEGukjofmANMiNw+1ifuxcCsWfZJWrcupKdbCyPF/PgjnHEGLFtmcxA9LJxLLkG6pPphe2qvB1DVOdjKtaUSkddFZKWILChyrJ+I/CwicyJfXUp4bGcR+VpElolI6g+FzpljfTT77Wdh0aRJ2BVVum++gdNOsxbGpEn2dp1zySVIYOxQ1TLm3Eb1BtA5yvFnVPXYyNcHxe8UkWrAEOBcoBXQQ0RaleP1k8O8ebaXRe3aFhaHHBJ2RZVu3jxbVHfrVnuLp5wSdkXOufIItPigiPQEqolICxF5HijzslpVnQasLUdN7YFlqvqdquYCI4Fu5XiexLdwIZx1lm16lJ5ul9CmmC++gN//3vawmDYNjjsu7Iqcc+UVJDBuB44GtgEjgI3AnRV4zdtEZF6kyyratOVGwE9FbmdGjqWWxYvhzDPtkzQ9HQ47LOyKKl16uuVh3bo2reTII8OuyDlXEWUGhqrmqOqDqnqCqqZFft5aztf7B3AYcCw2n+PpKOdEW6O0xL04RKSPiGSISMaqVavKWVacff21hYWIfaq2aBF2RZXuv/+1q4ObNbOwaNYs7IqccxUV5CqpNBEZLSKzIy2DeSIyrzwvpqq/qGqequYDr2DdT8VlYnM9CjQGskp5zqGRIEurX79+ecqKr2XLLCzy8+3S2SOOCLuiSjdiBFx0ERxzjM21SMGrg52rkoLM9H4b+AswH8ivyIuJyMGqmh252R3bnKm4L4EWItIc+Bm4HOhZkddNGN99Z/tv5+Zay6JV6o3lDx0KN91kl8+OG5eSq7A7V2UFCYxVqrrb8y5EZATQAagnIplAX6CDiByLdTEtB26MnNsQeFVVu6jqDhG5DfgIqAa8rqoLd/f1E87y5RYWOTnWsmjdOuyKKt3TT8M990CXLjYpr2bNsCtyzlUmKWurbhE5C1utdjI28A2Aqo6ObWm7Ly0tTTMyMsIuY1c//miXCq1fb2GRYpcKqULfvrb73aWX2nIfe+0VdlXOuSBEZJaqpgU5N0gLozdwJFCdwi4pBRIuMBJSZqa1LNats1VnUyws8vPhrrvg2WfhuutsmfJq1cKuyjkXC0ECo62qtol5JakoK8vCYvVqm96cFijEk0ZeHtxwAwwbZntwP/102ftwO+eSV5B5GJ+n9EzrWMnOtrBYscL24G4f7YKw5JWbCz16WFj06+dh4VxVEKSFcRpwtYh8j41hCKCqekxMK0tmv/xiM9Z+/tnC4uSTw66oUuXkwCWXwIcfwqBB1rpwzqW+IIERbT0oV5JVqywsfvjBPlFPOy3siirVxo1w3nkwfTq88gpcf33YFTnn4iXITO8fon3Fo7iElZ5uU5fT03c+vnq1hcV339n63WecEUp5sVLw9mbMsMl5HhbOVS1BxjBcUenp9if2Dz/Y94LQWLvW1uz+5hubsdaxY7h1VrKsLLsyeMECeO8924vbOVe1eGDsjoKwyMmx2zk5dnvcOAuLRYvs0/Tss8Ots5J9/70tT/7jj9bL1rVr2BU558IQZAzDwa5hUSAnB7p3t0uExo2zLVZTyOLFln9btsDkySl3sZdzbjd4CyOIksKiQH4+7Llnyq2FMXu2DcPk5dkigh4WzlVtHhhlKSssCmzbtvOYRpKbPt2GYfbZx35u41M3navyPDBKEzQsChSMaSR5aEycCOecAwcdZHtZHH542BU55xKBB0ZpevcOHhYFcnLscUlq9Gg4/3zbpuPTT6FJk7If45yrGjwwSjNsGNSqtXuPqVXLHpeEhg+HP/4R2rWzRlKDBmFX5JxLJB4YpenY0SbgBQ2NWrXs/CScgzFkCFx9tZU+cSLsv3/YFTnnEo0HRlmChkYSh8Xjj8Ntt0G3bvYWatcOuyLnXCKKWWCIyOsislJEFhQ5NlBElkT2BR8jIlH/jhWR5SIyX0TmiEj4OyKVFRpJGhaqcN998MADcMUV8O9/Q40aYVflnEtUsWxhvMGuCxdOAlpHVrpdCtxfyuM7quqxQXeCirmSQiNJwyI/H265Bf7+d9uDe/hwqF497Kqcc4ksZoGhqtOAtcWOTVTVHZGbnwONY/X6MVE8NJI0LLZvh1694KWX4N574cUXYQ/vnHTOlSHMj4lrgQ9LuE+BiSIyS0T6xLGmshWExiGHJGVYbN1qV0K9/TY89hg88YRvfOScCyaUtaRE5EFgB/B2CaecqqpZItIAmCQiSyItlmjP1QfoA9C0adOY1LuLjh1h+fL4vFYl+vVXuPBCWxPqhRfg1lvDrsg5l0zi3sIQkauB84ArVFWjnaOqWZHvK4ExQImrGKnqUFVNU9W0+vXrx6LklLB+vc3eTk+HN9/0sHDO7b64BoaIdAbuBS5Q1ahTqEVkHxGpU/AzcA6wINq5LpiVK6FDB8jIsCuhevUKuyLnXDKK5WW1I4AZwBEikiki1wEvAHWwbqY5IvJS5NyGIvJB5KEHAtNFZC4wExivqhNiVWeq++kn28ti6VIbcrnoorArcs4lq5iNYahqjyiHXyvh3CygS+Tn74C2saqrKlm2zLZUXb/eZm+n2Pbizrk48w2UUtT8+TZmsWOHjVscf3zYFTnnkp1ffZ+CZs60/bf32AOmTfOwcM5VDg+MFDN1qnVDHXCAbXx01FFhV+ScSxUeGClk/Hg491xo2tT2smjePOyKnHOpxAMjRYwaZZPyjj7a9t9u2DDsipxzqcYDIwW8+ir06AGnnAJTpkC9emFX5JxLRR4YSW7QILjhBujUCT78EPbdN+yKnHOpygMjSalCv35w9922mODYsbu/m6xzzu0On4eRhFThrrtg8GDo3RteeQWqVQu7KudcqvMWRpLJy7MuqMGD4Y47bPzCw8I5Fw8eGEkkNxd69oTXXoNHHoFnnvGNj5xz8eNdUkliyxa4+GIb2B44EO65J+yKnHNVjQdGEti4ES64wJb5ePll6JNYexA656oID4wEt2aNzd7+6ivbVrVHtDWAnXMuDjwwElh2NvzhD7ZM+ejRcP75YVfknKvKPDAS1PLlcPbZsGKFjVt07Bh2Rc65qi6m19iIyOsislJEFhQ59jsRmSQi30S+H1DCY6+OnPNNZB/wKmPJEtvsaO1amDzZw8I5lxhifVHmG0DnYsfuAyaragtgcuT2TkTkd0Bf4ESgPdC3pGBJNV99BWecYRsfTZ0KJ54YdkXOOWdiGhiqOg1YW+xwN+DNyM9vAhdGeWgnYJKqrlXVdcAkdg2elPO//1lromZNW578mGPCrsg55wqFMe3rQFXNBoh8bxDlnEbAT0VuZ0aOpaxJk2xL1QYNLCxatAi7Iuec21mizhOWKMc06okifUQkQ0QyVq1aFeOyYmPMGDjvPDj8cAuLpk3Drsg553YVRmD8IiIHA0S+r4xyTibQpMjtxkBWtCdT1aGqmqaqafXr16/0YmPtn/+01WaPP97GLA48MOyKnHMuujACYxxQcNXT1cDYKOd8BJwjIgdEBrvPiRxLKS++CL16we9/b11SB1SJYX3nXLKK9WW1I4AZwBEikiki1wFPAH8QkW+AP0RuIyJpIvIqgKquBQYAX0a++keOpYwnnoBbb7XJeOPHQ+3aYVfknHOlE9WoQwNJKS0tTTMyMsIuo1Sq8MADFhg9e8Ibb0D16mFX5ZyrqkRklqqmBTnXZ3rHUX4+3H67dUXdeCMMGeJ7WTjnkkeiXiWVcnbsgGuusbD4y1/gH//wsHDOJRdvYcTBtm22yuyYMfDXv1qXlES7cNg55xKYB0aMbd4M3bvbVVDPPWddUs45l4w8MGJo/Xro2hU+/xyGDbMuKeecS1YeGDGyciV06gQLF8I779j2qs45l8w8MGIgM9P2svjxRxg3Djqn/LKJzrmqwAOjki1bZmGxdi189BGcfnrYFTnnXOXwwKhECxbYlqrbt0N6OrRrF3ZFzjlXeXweRiX58ktbE0oEpk3zsHDOpR4PjHLIzrZwWLHCbn/yCZx5Juy3H0yfDq1ahVufc87FggdGOQwYYMEwYAB88IENajdpYntZHHpo2NU551xs+OKDuyk720Jh61bYay/Iy4O2bW2Au169mL60c85VOl98MIYGDLBFBAFyc+Ggg2DKFOuOcs65VOZdUrshO9tmbOfmFh7bsAG2bAmvJuecixcPjN1QtHVRIC/PjjvnXKqLe2CIyBEiMqfI10YRubPYOR1EZEORcx6Jd53FRWtdgN0eNqzwiinnnEtVcR/DUNWvgWMBRKQa8DMwJsqpn6rqefGsrTTRWhcFCloZQ4bEtybnnIunsLukzgK+VdUfQq6jVCW1Lgp4K8M5VxWEHRiXAyNKuO9kEZkrIh+KyNElPYGI9BGRDBHJWLVqVUyKLK11UcDHMpxzqS60wBCRvYALgH9HuXs2cIiqtgWeB94r6XlUdaiqpqlqWv369WNS64wZJbcuCuTmwmefxeTlnXMuIYQ5D+NcYLaq/lL8DlXdWOTnD0TkRRGpp6qr41phxFdfhfGqzjmXWMLskupBCd1RInKQiO16LSLtsTrXxLE255xzxYTSwhCRWsAfgBuLHLsJQFVfAi4BbhaRHcAW4HJNpTVMnHMuCYUSGKqaA9QtduylIj+/ALwQ77qcc86VLOyrpJxzziUJDwznnHOBeGA455wLxAPDOedcIB4YzjnnAvHAcM45F4gHhnPOuUA8MJxzzgUiqTSBWkRWAWUtlV4PCGVNqlJ4TcEkYk2QmHV5TcF4TbbQa6CVW1MqMIIQkQxVTQu7jqK8pmASsSZIzLq8pmC8pt3jXVLOOecC8cBwzjkXSFUMjKFhFxCF1xRMItYEiVmX1xSM17QbqtwYhnPOufKpii0M55xz5ZCygSEinUXkaxFZJiL3lXLeJSKiIhLzqxKC1CQil4rIIhFZKCL/CrsmEWkqIuki8pWIzBORLnGo6XURWSkiC0q4X0TkuUjN80Tk+ASo6YpILfNE5DMRaRt2TUXOO0FE8kTkkkSoSUQ6iMicyO/4J2HXJCL7ich/RWRupKbecaipSeT/q8WR17wjyjlx/z0vk6qm3BdQDfgWOBTYC5gLtIpyXh1gGvA5kBZ2TUAL4CvggMjtBglQ01Dg5sjPrYDlcfj3OwM4HlhQwv1dgA8BAU4CvkiAmk4p8u92biLUVOTfeArwAXBJ2DUB+wOLgKaR2zH9HQ9Y0wPA3yM/1wfWAnvFuKaDgeMjP9cBlkb5fy/uv+dlfaVqC6M9sExVv1PVXGAk0C3KeQOAJ4GtCVLTDcAQVV0HoKorE6AmBfaN/LwfkBXjmlDVadj/tCXpBgxX8zmwv4gcHGZNqvpZwb8b9gdI41jWE6SmiNuBd4FY/y4BgWrqCYxW1R8j58e8rgA1KVBHRASoHTl3R4xrylbV2ZGfNwGLgUbFTov773lZUjUwGgE/FbmdSbF/DBE5Dmiiqu8nSk1AS6CliPxPRD4Xkc4JUFM/4EoRycT+Sr09xjUFEaTuMF2H/WUYKhFpBHQHXirr3DhqCRwgIlNFZJaI9Aq7IGw76KOwP4bmA3eoan68XlxEmgHHAV8Uuyvhfs9D2dM7DiTKsd8uBxORPYBngGviVRBl1BSxJ9Yt1QH7C/VTEWmtqutDrKkH8IaqPi0iJwP/jNQUt/+hoghSdyhEpCMWGKeFXQswGLhXVfPsj+eEsCfQDjgLqAnMEJHPVXVpiDV1AuYAZwKHAZNE5FNV3RjrFxaR2lgL8M4or5dwv+ep2sLIBJoUud2YnbtS6gCtgakishzrHxwX44HvsmoqOGesqm5X1e+Br7EACbOm64B3AFR1BlADW+smTEHqjjsROQZ4FeimqmvCrgdIA0ZGfscvAV4UkQvDLYlMYIKqblbV1dgYYswvEChDb6ybTFV1GfA9cGSsX1REqmNh8baqjo5ySsL9nqdqYHwJtBCR5iKyF3A5MK7gTlXdoKr1VLWZqjbD+pwvUNWMsGqKeA/oCCAi9bDm+3ch1/Qj9tcgInIUFhirYlhTEOOAXpGrSE4CNqhqdpgFiUhTYDRwVch/Lf9GVZsX+R3/D3CLqr4XclljgdNFZE8RqQWciPXfh6no7/iBwBHE9v87IuMlrwGLVXVQCacl3O95SnZJqeoOEbkN+Ai7SuR1VV0oIv2BDFUt/qGYKDV9BJwjIouAPOAvsfxLNWBNdwOviMifsebwNRq5hCNWRGQE1i1XLzJ20heoHqn5JWwspQuwDMjB/kKMqQA1PQLUxf6KB9ihMV5ALkBNcVdWTaq6WEQmAPOAfOBVVS31suBY14Rd/PKGiMzHuoHujbR+YulU4CpgvojMiRx7AGhapK64/56XxWd6O+ecCyRVu6Scc85VMg8M55xzgXhgOOecC8QDwznnXCAeGM455wLxwHCukohIPxG5J+w6nIsVDwznnHOBeGA4VwEi8qDYfiIfYzOEEZFjI4tHzhORMSJyQOT4n8T2OpknIiMjx/aJ7NfwpdieI9FWVXYuIfjEPefKSUTaAW9gy1vsCczGVobtBdyuqp9EZs3vq6p3ikgW0FxVt4nI/qq6XkQeAxap6lsisj8wEzhOVTeH8qacK4W3MJwrv9OBMaqaE1lpdBywD7C/qhbsJPcmtoEP2HIYb4vIlRTut3AOcF9keYip2FpdTeNUv3O7JSXXknIujnanid4VC48LgIdF5Ghs7aKLVfXrWBTnXGXyFoZz5TcN6C4iNUWkDnA+sBlYJyKnR865CvgksgdLE1VNB/4P26q0Nrbw4+2R1UsLNvZyLiH5GIZzFSAiD2JjFj9g+xcsAj7GxjJqYctk9wZ+BdKxbW4FeEtVnxCRmthGR6dEji9X1fPi/T6cC8IDwznnXCDeJeWccy4QDwznnHOBeGA455wLxAPDOedcIB4YzjnnAvHAcM45F4gHhnPOuUA8MJxzzgXy/yLk8pPThXkOAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from statsmodels.graphics.factorplots import interaction_plot\n",
    "from scipy import stats\n",
    "data = pd.read_csv(\"C:/Users/rushb/Downloads/ToothGrowth.csv\")\n",
    "fig=interaction_plot(data.dose,data.supp,data.len,colors=['red','blue'], markers=['D','^'], ms=10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "N = len(data.len)\n",
    "df_a = len(data.supp.unique()) - 1\n",
    "df_b = len(data.dose.unique()) - 1\n",
    "df_axb = df_a*df_b \n",
    "df_w = N - (len(data.supp.unique())*len(data.dose.unique()))\n",
    "grand_mean = data['len'].mean()\n",
    "ssq_a = sum([(data[data.supp ==i].len.mean()-grand_mean)**2 for i in data.supp])\n",
    "ssq_b = sum([(data[data.dose ==i].len.mean()-grand_mean)**2 for i in data.dose])\n",
    "ssq_t = sum((data.len - grand_mean)**2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "205.35000000000005"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ssq_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "205.35000000000005\n"
     ]
    }
   ],
   "source": [
    "x=0\n",
    "for i in data.supp:\n",
    "    x=x + (data[data.supp ==i].len.mean()-grand_mean)**2\n",
    "    ssq=x\n",
    "print(ssq)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "108.31900000000155\n"
     ]
    }
   ],
   "source": [
    "vc =data[data.supp == 'VC']\n",
    "oj =data[data.supp == 'OJ']\n",
    "vc_dose_means = [vc[vc.dose==d].len.mean() for d in vc.dose]\n",
    "oj_dose_means =[oj[oj.dose==d].len.mean() for d in oj.dose]\n",
    "\n",
    "ssq_w=sum((oj.len- oj_dose_means)**2) + sum((vc.len-vc_dose_means)**2)\n",
    "\n",
    "ssq_axb = ssq_t - ssq_a - ssq_b -ssq_w\n",
    "\n",
    "print(ssq_axb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "ms_a = ssq_a/df_a\n",
    "ms_b = ssq_b/df_b\n",
    "ms_axb = ssq_axb/df_axb\n",
    "ms_w = ssq_w/df_w\n",
    "f_a = ms_a/ms_w\n",
    "f_b = ms_b/ms_w\n",
    "f_axb = ms_axb/ms_w"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "p_a = stats.f.sf(f_a, df_a, df_w)\n",
    "p_b = stats.f.sf(f_b, df_b, df_w)\n",
    "p_axb = stats.f.sf(f_axb, df_axb, df_w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sum_sq</th>\n",
       "      <th>df</th>\n",
       "      <th>F</th>\n",
       "      <th>PR(&gt;F)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>supp</th>\n",
       "      <td>205.350000</td>\n",
       "      <td>1</td>\n",
       "      <td>15.572</td>\n",
       "      <td>0.000231183</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dose</th>\n",
       "      <td>2426.434333</td>\n",
       "      <td>2</td>\n",
       "      <td>92</td>\n",
       "      <td>4.04629e-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>supp:dose</th>\n",
       "      <td>108.319000</td>\n",
       "      <td>2</td>\n",
       "      <td>4.10699</td>\n",
       "      <td>0.0218603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Residual</th>\n",
       "      <td>712.106000</td>\n",
       "      <td>54</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                sum_sq  df        F       PR(>F)\n",
       "supp        205.350000   1   15.572  0.000231183\n",
       "dose       2426.434333   2       92  4.04629e-18\n",
       "supp:dose   108.319000   2  4.10699    0.0218603\n",
       "Residual    712.106000  54      NaN          NaN"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results = {'sum_sq':[ssq_a,ssq_b,ssq_axb,ssq_w],\n",
    "            'df':[df_a,df_b,df_axb,df_w],\n",
    "             'F':[f_a,f_b,f_axb,'NaN'],\n",
    "              'PR(>F)':[p_a,p_b,p_axb,'NaN']}\n",
    "columns=['sum_sq','df','F','PR(>F)']\n",
    "\n",
    "aov_table1=pd.DataFrame(results,columns=columns,index=['supp','dose','supp:dose','Residual'])\n",
    "\n",
    "aov_table1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
