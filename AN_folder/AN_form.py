from flask import Flask, request, render_template

app = Flask(__name__)

atomicnumber_symbol = [   'H', "He",
                          "Li", "Be", "B", 'C', 'N', "O", "F", "Ne", 
                          "Na", "Mg", "Al", "Si", 'P', 'S', "Cl", "Ar", 
                          'K', "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", 
                          "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", 
                          "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", 
                          "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
metals = {
    1 : "No", 2 : "No",
    5 : "Semi", 6 : "No", 7 : "No", 8 : "No", 9 : "No", 10 : "No",
    14 : "semi", 15 : "No", 16 : "No", 17 : "No", 18 : "No",
    32 : "Semi", 33 : "Semi", 34 : "No", 35 : "No", 36 : "No",
    51 : "Semi", 52 : "Semi", 53 : "No",  54 :  "No", 
    84 :  "Semi", 85 : "Semi", 86 : "No",
    117 : "Semi", 118 : "No"
    }


atomicnumber_name = [ 
    "Hydrogen", "Helium",
    "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
    "Potassium", "calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt","Nickel", "Copper", "Zink", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton",
    "Rebidium", "Strontium", "Yttrium", "Zirconium", "Noibium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Candmium", "Indium", "Tin", "Anitmony", "Tellurium", "Iodine", "Xenon",
    "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungesten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon",
    "Francium", "Radium", "Actinium", "Thorium", "Protctinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einstenium", "Fermium", "Mondelevium", "Nopelium", "Lawrencium", "Ratherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]

state_of_matter = {
    1 : 'g', 2 : 'g',
    7 : 'g', 8 : 'g', 9 : 'g', 10 : 'g',
    17 : "g", 18 : "g",
    35 : "l", 37 : "g",
    43 : "s", 54 : "g", #s means >> synthetic elements
    61 : "s",  80 : "l", 86 : "g",
}

Valence_E= {
    1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0
}

counter_ = 0

AN_C = {}

def start ():
    #Valence_E.clear()

    for i in range(1, 8, 1):
        Valence_E[i] = 0

    
    #if counter_ != 0: counter_ = 0

    AN_C.clear()

    for i in Valence_E:
        if  Valence_E[i] != 0: return '0'
    
    if counter_ != 0: return '0'

    for i in AN_C:
       return '0'

    return '1'


NG = [2, 10, 18, 36, 54, 86, 118]

def GSAN(atomic_number):
    answer_symbol =  (atomicnumber_symbol[atomic_number - 1])

    return answer_symbol

def GMAN (atomic_number):
    answer_metal = " "
    if atomic_number not in metals:
        answer_metal = ("فلز ")
    elif metals[atomic_number] == "Semi":
        answer_metal = ("شبه فلز ")
    elif metals[atomic_number] == "No":
        answer_metal =  ("لا فلز ")
    return answer_metal 

def GSMAN (atomic_number):
    answer_States = " "
    if atomic_number not in state_of_matter and atomic_number < 93:
        answer_States = (" صلب ")
    elif atomic_number >= 93 or state_of_matter[atomic_number] == "s":
        answer_States = (" مصنع ")
    elif state_of_matter[atomic_number] == "g":
        answer_States = (" غاز ")
    elif state_of_matter[atomic_number] == "l":
        answer_States =  (" سائل ")
    return answer_States

def GNAN (atomic_number):
    return atomicnumber_name[atomic_number - 1]

def GEC_s (PQN, atomic_number, counter):
    ans = str(PQN)
    if atomic_number >= 2:
        Valence_E[PQN] += 2
        ans +=  "s(2) " + GECAN (atomic_number -2, counter +1)
    elif atomic_number == 1:
        Valence_E[PQN] += 1
        ans +=  "s(1) " 
    return ans
        
def GEC_p (PQN, atomic_number, counter):
    ans = str(PQN)
    if atomic_number >= 6:
        Valence_E[PQN] += 6
        ans += "p(6) " + GECAN(atomic_number-6, counter +1)
    elif atomic_number >= 1:
        Valence_E[PQN] += atomic_number
        ans += "p(" + str(atomic_number) + ") " 
    return ans

def GEC_d (PQN, atomic_number, counter):
    ans = str(PQN)
    if atomic_number >= 10:
        Valence_E[PQN] += 10
        ans += "d(10) " + GECAN (atomic_number -10, counter +1)
    elif atomic_number >= 1:
        Valence_E[PQN] += atomic_number
        ans += "d(" + str(atomic_number) + ") " 
    return ans

def GEC_f (PQN, atomic_number, counter): 
    ans = str(PQN)
    if atomic_number >= 14:
        Valence_E[PQN] += 14
        ans += "f(14) " + GECAN (atomic_number -14, counter +1)
    elif atomic_number >= 1:
        Valence_E[PQN] += atomic_number
        ans += "f(" + str(atomic_number) + ") " 
    return ans
    
def GECAN (atomic_number, counter):
    PQN  = [1, 2, 2, 3, 3, 4, 3, 4, 5, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7]
    SEL = ['s', 's', 'p', 's', 'p', 's', 'd', 'p', 's', 'd', 'p', 's', 'f', 'd', 'p', 's', 'f', 'd', 'p']
    answer = ' '
    AN_C[atomic_number] = counter
    if atomic_number == 0: 
        return ''
    
    if (SEL[counter] == 's'): 
        answer += GEC_s(PQN[counter], atomic_number, counter)
    elif (SEL[counter] == 'p'): 
        answer += GEC_p(PQN[counter], atomic_number, counter)
    elif (SEL[counter] == 'd'):
        answer += GEC_d(PQN[counter], atomic_number, counter)
    elif (SEL[counter] == 'f'):
        answer += GEC_f(PQN[counter], atomic_number, counter)

    AN_C[atomic_number] = counter
    return answer
def GVE ():
    ans = 0
    for i in range (1, 8, 1):
        if Valence_E[i] > 0:
            ans = Valence_E[i]
    return ans

def GECG (atomic_number, ve):
    counter_2 = 0
    for i in AN_C:
        counter_ = max(i, counter_2)
        counter_2 = i
    val = int()
    if (atomic_number == 1): return "لا يوجد"
    #if (ve == 8):
        
        #return "[" + GSAN(atomic_number)+ "]"
    for i in NG:
        if atomic_number < i: break
        val = i
        answer = "[" + GSAN(i) + "]: "
    No_thing = GECAN(val, 0)
    counter_2 = 0
    for i in AN_C:
        counter_ = max(AN_C[i], counter_2)
        counter_2 = AN_C[i]

    answer += GECAN(atomic_number - val, counter_)

    return answer



@app.route("/")
def form_page_atomicnumber():
    return render_template("form.html")

@app.route("/process", methods=["POST"])
def process_data_atomicnumber():
    result = int(request.form["atomic"])

    if result > 118 or result < 1:
        return "Error"
    
    #check = start()
    #if check != '1': return "False"

    name = GNAN(result)
    text = "خصائص العنصر"
    metal = GMAN(result)
    state = "- " + GSMAN(result)
    num1 = "العدد الذري: "
    num2 = str(result)
    symbol1 = "رمز العنصر: " 
    symbol2 = GSAN(result)
    EC1 = "التوزيع الإلكتروني: "
    EC2 = GECAN(result, 0)
    VE1 = "إلكترونات التكافؤ: "
    VE2 = str(GVE())
    ECG1 = "التوزيع المختصر: "
    ECG2 = GECG(result, GVE()) 
    return render_template("form.html", name=name, text=text, symbol1=symbol1, metal=metal, state=state, symbol2=symbol2, EC1=EC1, EC2=EC2, VE1=VE1, VE2=VE2, ECG1=ECG1, ECG2=ECG2, num1=num1, num2=num2)


app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    app.run(debug=True)


