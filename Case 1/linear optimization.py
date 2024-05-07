# Imports
import sys
from pulp import LpMaximize, LpProblem, LpVariable


def calculate_supplier_selection():
    ### Initialize model
    model = LpProblem(name='Car Production', sense=LpMaximize)

    ########################################################################################
    ###################################### Variables #######################################
    ########################################################################################

    ### Represents the amount of steel provided by a company. The variable is continuous,
    ### meaning that it can take any real value greater than zero
    steel_amount_east_metal = LpVariable(name='steel_amount_east_metal', lowBound=0, cat='Continuous')
    steel_amount_sakura = LpVariable(name='steel_amount_sakura', lowBound=0, cat='Continuous')
    steel_amount_black_forest = LpVariable(name='steel_amount_black_forest', lowBound=0, cat='Continuous')

    ### Binary variable that indicates whether the companies steel is used or not. If the variable equals 1,
    ### it means that the company's steel is used. If it equals 0, it means that the company does not provide steel
    use_steel_east_metal = LpVariable(name='use_steel_east_metal', lowBound=0, cat='Binary')
    use_steel_sakura = LpVariable(name='use_steel_sakura', lowBound=0, cat='Binary')
    use_steel_black_forest = LpVariable(name='use_steel_black_forest', lowBound=0, cat='Binary')

    ### Represents the amount of aluminium provided by a company. The variable is continuous,
    ### meaning that it can take any real value greater than zero
    aluminium_amount_rising_sun = LpVariable(name='aluminium_amount_rising_sun', lowBound=0, cat='Continuous')
    aluminium_amount_rhine_metal = LpVariable(name='aluminium_amount_rhine_metal', lowBound=0, cat='Continuous')
    aluminium_amount_fjordlight = LpVariable(name='aluminium_amount_fjordlight', lowBound=0, cat='Continuous')

    ### Binary variable that indicates whether the company's aluminium is used or not. If the variable equals 1,
    ### it means that the company's aluminium is used. If it equals 0, it means that the company does not provide aluminium
    use_aluminium_rising_sun = LpVariable(name='use_aluminium_rising_sun', lowBound=0, cat='Binary')
    use_aluminium_rhine_metal = LpVariable(name='use_aluminium_rhine_metal', lowBound=0, cat='Binary')
    use_aluminium_fjordlight = LpVariable(name='use_aluminium_fjordlight', lowBound=0, cat='Binary')

    ### Represents the amount of microchips provided by a company. The variable is continuous,
    ### meaning that it can take any real value greater than zero
    microchips_amount_skytech = LpVariable(name='microchips_amount_skytech', lowBound=0, cat='Continuous')
    microchips_amount_sic = LpVariable(name='microchips_amount_sic', lowBound=0, cat='Continuous')
    microchips_amount_nexgen = LpVariable(name='microchips_amount_nexgen', lowBound=0, cat='Continuous')

    ### Binary variable that indicates whether the company's microchips are used or not. If the variable equals 1,
    ### it means that the company's microchips are used. If it equals 0, it means that the company does not provide microchips
    use_microchips_skytech = LpVariable(name='use_microchips_skytech', lowBound=0, cat='Binary')
    use_microchips_sic = LpVariable(name='use_microchips_sic', lowBound=0, cat='Binary')
    use_microchips_nexgen = LpVariable(name='use_microchips_nexgen', lowBound=0, cat='Binary')

    ### Represents the amount of cobalt provided by a company. The variable is continuous,
    ### meaning that it can take any real value greater than zero
    cobalt_amount_congo_cobalt = LpVariable(name='cobalt_amount_congo_cobalt', lowBound=0, cat='Continuous')
    cobalt_amount_auric_cobalt = LpVariable(name='cobalt_amount_auric_cobalt', lowBound=0, cat='Continuous')
    cobalt_amount_ncc = LpVariable(name='cobalt_amount_ncc', lowBound=0, cat='Continuous')

    ### Binary variable that indicates whether the company's cobalt is used or not. If the variable equals 1,
    ### it means that the company's cobalt is used. If it equals 0, it means that the company does not provide cobalt
    use_cobalt_congo_cobalt = LpVariable(name='use_cobalt_congo_cobalt', lowBound=0, cat='Binary')
    use_cobalt_auric_cobalt = LpVariable(name='use_cobalt_auric_cobalt', lowBound=0, cat='Binary')
    use_cobalt_ncc = LpVariable(name='use_cobalt_ncc', lowBound=0, cat='Binary')

    ### Represents the amount of lithium provided by a company. The variable is continuous,
    ### meaning that it can take any real value greater than zero
    lithium_amount_sollith = LpVariable(name='lithium_amount_sollith', lowBound=0, cat='Continuous')
    lithium_amount_litio_andes = LpVariable(name='lithium_amount_litio_andes', lowBound=0, cat='Continuous')
    lithium_amount_lithiumoz = LpVariable(name='lithium_amount_lithiumoz', lowBound=0, cat='Continuous')

    ### Binary variable that indicates whether the company's lithium is used or not. If the variable equals 1,
    ### it means that the company's lithium is used. If it equals 0, it means that the company does not provide lithium
    use_lithium_chile_sollith = LpVariable(name='use_lithium_chile_sollith', lowBound=0, cat='Binary')
    use_lithium_litio_andes = LpVariable(name='use_lithium_litio_andes', lowBound=0, cat='Binary')
    use_lithium_lithiumoz = LpVariable(name='use_lithium_lithiumoz', lowBound=0, cat='Binary')

    ### Number of cars produced
    car_amount = LpVariable(name='car_amount', lowBound=0, cat='Integer')

    ########################################################################################
    ###################################### Constants #######################################
    ########################################################################################

    ### Steel prices at various companies
    steel_price_east_metal = 1
    steel_price_sakura = 1
    steel_price_black_forest = 1

    ### Aluminium prices at various companies
    aluminium_price_rising_sun = 1
    aluminium_price_rhine_metal = 1
    aluminium_price_fjordlight = 1

    ### Microchips prices at various companies
    microchips_price_skytech = 1
    microchips_price_sic = 1
    microchips_price_nexgen = 1

    ### Cobalt prices at various companies
    cobalt_price_congo_cobalt = 1
    cobalt_price_auric_cobalt = 1
    cobalt_price_ncc = 1

    ### Lithium prices at various companies
    lithium_price_sollith = 1
    lithium_price_litio_andes = 1
    lithium_price_lithiumoz = 1

    ### Material demand per car
    steel_demand = 600
    aluminium_demand = 90
    microchips_demand = 1200
    cobalt_demand = 15
    lithium_demand = 14

    ### Production budget
    budget = 1000000

    ### Helpers
    M = sys.maxsize

    ########################################################################################
    ##################################### Constraints ######################################
    ########################################################################################

    ### Calculate the amount of steel required per car by summing
    ### the steel amounts from three different sources
    steel_per_car = car_amount == steel_amount_east_metal * (1 / steel_demand) \
                    + steel_amount_black_forest * (1 / steel_demand) \
                    + steel_amount_sakura * (1 / steel_demand)
    model += (steel_per_car, "steel_per_car")

    ### Enforce a constraint that allows only one steel supplier to be used for the optimization by setting the
    ### upper bound of the steel amount for each supplier to be M (a very large number) times their respective
    ### binary decision variables. This ensures that the amount of steel from a particular supplier is zero if
    ### the corresponding binary variable is not selected
    one_steel_east_metal = steel_amount_east_metal <= M * use_steel_east_metal
    model += (one_steel_east_metal, "one_steel_east_metal")
    one_steel_sakura = steel_amount_sakura <= M * use_steel_sakura
    model += (one_steel_sakura, "one_steel_sakura")
    one_steel_black_forest = steel_amount_black_forest <= M * use_steel_black_forest
    model += (one_steel_black_forest, "one_steel_black_forest")
    only_one_steel = 1 >= one_steel_east_metal + one_steel_black_forest + one_steel_sakura
    model += only_one_steel

    ### Calculate the amount of aluminium required per car by summing
    ### the steel amounts from three different sources
    aluminium_per_car = car_amount == aluminium_amount_rising_sun * (1 / aluminium_demand) \
                        + aluminium_amount_rhine_metal * (1 / aluminium_demand) \
                        + aluminium_amount_fjordlight * (1 / aluminium_demand)
    model += (aluminium_per_car, "aluminium_per_car")

    ### Enforce a constraint that allows only one aluminium supplier to be used for the optimization by setting the
    ### upper bound of the aluminium amount for each supplier to be M (a very large number) times their respective
    ### binary decision variables. This ensures that the amount of aluminium from a particular supplier is zero if
    ### the corresponding binary variable is not selected
    one_aluminium_rising_sun = aluminium_amount_rising_sun <= M * use_aluminium_rising_sun
    model += (one_aluminium_rising_sun, "one_aluminium_rising_sun ")
    one_aluminium_rhine_metal = aluminium_amount_rhine_metal <= M * use_aluminium_rhine_metal
    model += (one_aluminium_rhine_metal, "one_aluminium_rhine_metal")
    one_aluminium_fjordlight = aluminium_amount_fjordlight <= M * use_aluminium_fjordlight
    model += (one_aluminium_fjordlight, "one_aluminium_fjordlight")
    only_one_aluminium = 1 >= one_aluminium_rising_sun + one_aluminium_rhine_metal + one_aluminium_fjordlight
    model += only_one_aluminium

    ### Calculate the amount of microchips required per car by summing
    ### the steel amounts from three different sources
    microchips_per_car = car_amount == microchips_amount_skytech * (1 / microchips_demand) \
                         + microchips_amount_sic * (1 / microchips_demand) \
                         + microchips_amount_nexgen * (1 / microchips_demand)
    model += (microchips_per_car, "microchips_per_car")

    ### Enforce a constraint that allows only one microchip supplier to be used for the optimization by setting the
    ### upper bound of the microchip amount for each supplier to be M (a very large number) times their respective
    ### binary decision variables. This ensures that the amount of microchips from a particular supplier is zero if
    ### the corresponding binary variable is not selected
    one_microchips_skytech = microchips_amount_skytech <= M * use_microchips_skytech
    model += (one_microchips_skytech, "one_microchips_skytech")
    one_microchips_sic = microchips_amount_sic <= M * use_microchips_sic
    model += (one_microchips_sic, "one_microchips_sic")
    one_microchips_nexgen = microchips_amount_nexgen <= M * use_microchips_nexgen
    model += (one_microchips_nexgen, "one_microchips_nexgen")
    only_one_microchips = 1 >= one_microchips_skytech + one_microchips_sic + one_microchips_nexgen
    model += only_one_microchips

    #### Calculate the amount of cobalt required per car by summing
    ### the steel amounts from three different sources
    cobalt_per_car = car_amount == cobalt_amount_congo_cobalt * (1 / cobalt_demand) \
                     + cobalt_amount_auric_cobalt * (1 / cobalt_demand) \
                     + cobalt_amount_ncc * (1 / cobalt_demand)
    model += (cobalt_per_car, "cobalt_per_car")

    ### Enforce a constraint that allows only one cobalt supplier to be used for the optimization by setting the
    ### upper bound of the cobalt amount for each supplier to be M (a very large number) times their respective
    ### binary decision variables. This ensures that the amount of cobalt from a particular supplier is zero if
    ### the corresponding binary variable is not selected
    one_cobalt_congo_cobalt = cobalt_amount_congo_cobalt <= M * use_cobalt_congo_cobalt
    model += (one_cobalt_congo_cobalt, "one_cobalt_congo_cobalt")
    one_cobalt_auric_cobalt = cobalt_amount_auric_cobalt <= M * use_cobalt_auric_cobalt
    model += (one_cobalt_auric_cobalt, "one_cobalt_auric_cobalt")
    one_cobalt_ncc = cobalt_amount_ncc <= M * use_cobalt_ncc
    model += (one_cobalt_ncc, "one_cobalt_ncc")
    only_one_cobalt = 1 >= one_cobalt_congo_cobalt + one_cobalt_auric_cobalt + one_cobalt_ncc
    model += only_one_cobalt

    ### Calculate the amount of lithium required per car by summing
    ### the steel amounts from three different sources
    lithium_per_car = car_amount == lithium_amount_sollith * (1 / lithium_demand) \
                      + lithium_amount_litio_andes * (1 / lithium_demand) \
                      + lithium_amount_lithiumoz * (1 / lithium_demand)
    model += (lithium_per_car, "lithium_per_car")

    ### Enforce a constraint that allows only one lithium supplier to be used for the optimization by setting the
    ### upper bound of the lithium amount for each supplier to be M (a very large number) times their respective
    ### binary decision variables. This ensures that the amount of lithium from a particular supplier is zero if
    ### the corresponding binary variable is not selected
    one_lithium_sollith = lithium_amount_sollith <= M * use_lithium_chile_sollith
    model += (one_lithium_sollith, "one_lithium_sollith")
    one_lithium_litio_andes = lithium_amount_litio_andes <= M * use_lithium_litio_andes
    model += (one_lithium_litio_andes, "one_lithium_litio_andes")
    one_lithium_lithiumoz = lithium_amount_lithiumoz <= M * use_lithium_lithiumoz
    model += (one_lithium_lithiumoz, "one_lithium_lithiumoz")
    only_one_lithium = 1 >= one_lithium_sollith + one_lithium_litio_andes + one_lithium_lithiumoz
    model += only_one_lithium

    ### Enforce a budget constraint by calculating the total cost of all materials required for the car,
    ### and lithium, and ensuring that the cost does not exceed the available budget
    budget_constraint = budget >= steel_amount_east_metal * steel_price_east_metal \
                        + steel_amount_sakura * steel_price_sakura \
                        + steel_amount_black_forest * steel_price_black_forest \
                        + aluminium_amount_rising_sun * aluminium_price_rising_sun \
                        + aluminium_amount_rhine_metal * aluminium_price_rhine_metal \
                        + aluminium_amount_fjordlight * aluminium_price_fjordlight \
                        + microchips_amount_skytech * microchips_price_skytech \
                        + microchips_amount_sic * microchips_price_sic \
                        + microchips_amount_nexgen * microchips_price_nexgen \
                        + cobalt_amount_congo_cobalt * cobalt_price_congo_cobalt \
                        + cobalt_amount_auric_cobalt * cobalt_price_auric_cobalt \
                        + cobalt_amount_ncc * cobalt_price_ncc \
                        + lithium_amount_sollith * lithium_price_sollith \
                        + lithium_amount_litio_andes * lithium_price_litio_andes \
                        + lithium_amount_lithiumoz * lithium_price_lithiumoz
    model += (budget_constraint, "budget_constraint")

    ########################################################################################
    ##################################### Solve model ######################################
    ########################################################################################

    # Set goal function
    obj_func = car_amount
    model += obj_func

    # Solve model
    status = model.solve()

    ########################################################################################
    ################################### Output results #####################################
    ########################################################################################

    print("\n#################### Production ####################")
    print("### Number of cars produced ####")
    print("Number of cars produced: " + str(car_amount.value()))

    print("\n################## Materials ##################")
    print("### Steel")
    print("Amount of steel (East Metal Co.): " + str(steel_amount_east_metal.value()))
    print("Amount of steel (Sakura Steelworks): " + str(steel_amount_sakura.value()))
    print("Amount of steel (Black Forest Steel Co.): " + str(steel_amount_black_forest.value()))
    print("### Aluminium")
    print("Amount of aluminium (Rising Sun Aluminium): " + str(aluminium_amount_rising_sun.value()))
    print("Amount of aluminium (RhineMetal Aluminium): " + str(aluminium_amount_rhine_metal.value()))
    print("Amount of aluminium (Fjordlight Aluminium): " + str(aluminium_amount_fjordlight.value()))
    print("### Microchips")
    print("Amount of microchips (Skytech Microelectronics Ltd.): " + str(microchips_amount_skytech.value()))
    print("Amount of microchips (Silicon Innovations Corporation): " + str(microchips_amount_sic.value()))
    print("Amount of microchips (NexGen Microsystems GmbH): " + str(microchips_amount_nexgen.value()))
    print("### Cobalt")
    print("Amount of cobalt (Congo Cobalt): " + str(cobalt_amount_congo_cobalt.value()))
    print("Amount of cobalt (AuricCobalt): " + str(cobalt_amount_auric_cobalt.value()))
    print("Amount of cobalt (NCC): " + str(cobalt_amount_ncc.value()))
    print("### Lithium")
    print("Amount of lithium (SolLith): " + str(lithium_amount_sollith.value()))
    print("Amount of lithium (LitioAndes): " + str(lithium_amount_litio_andes.value()))
    print("Amount of lithium (LithiumOz): " + str(lithium_amount_lithiumoz.value()))

    print("\n################### Costs ###################")
    print("### Steel")
    print("Costs of steel (East Metal Co.): " + str(steel_amount_east_metal.value() * steel_price_east_metal))
    print("Costs of steel (Sakura Steelworks): " + str(steel_amount_sakura.value() * steel_price_sakura))
    print(
        "Costs of steel (Black Forest Steel Co.): " + str(steel_amount_black_forest.value() * steel_price_black_forest))
    print("### Aluminium")
    print("Costs of aluminium (Rising Sun Aluminium): " + str(
        aluminium_amount_rising_sun.value() * aluminium_price_rising_sun))
    print("Costs of aluminium (RhineMetal Aluminium): " + str(
        aluminium_amount_rhine_metal.value() * aluminium_price_rhine_metal))
    print("Costs of aluminium (Fjordlight Aluminium): " + str(
        aluminium_amount_fjordlight.value() * aluminium_price_fjordlight))
    print("### Microchips")
    print("Costs of microchips (Skytech Microelectronics Ltd.): " + str(
        microchips_amount_skytech.value() * microchips_price_skytech))
    print("Costs of microchips (Silicon Innovations Corporation): " + str(
        microchips_amount_sic.value() * microchips_price_sic))
    print("Costs of microchips (NexGen Microsystems GmbH): " + str(
        microchips_amount_nexgen.value() * microchips_price_nexgen))
    print("### Cobalt")
    print("Costs of cobalt (Congo Cobalt): " + str(cobalt_amount_congo_cobalt.value() * cobalt_price_congo_cobalt))
    print("Costs of cobalt (AuricCobalt): " + str(cobalt_amount_auric_cobalt.value() * cobalt_price_auric_cobalt))
    print("Costs of cobalt (NCC): " + str(cobalt_amount_ncc.value() * cobalt_price_ncc))
    print("### Lithium")
    print("Costs of lithium (SolLith): " + str(lithium_amount_sollith.value() * lithium_price_sollith))
    print("Costs of lithium (LitioAndes): " + str(lithium_amount_litio_andes.value() * lithium_price_litio_andes))
    print("Costs of lithium (LithiumOz): " + str(lithium_amount_lithiumoz.value() * lithium_price_lithiumoz))


if __name__ == "__main__":
    calculate_supplier_selection()
