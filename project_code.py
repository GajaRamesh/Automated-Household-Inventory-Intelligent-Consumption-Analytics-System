# Step 1: Display inventory status and advice

item_name = "Rice"
available_stock = 8
daily_usage = 2

print("Household Inventory Details")
print("Item Name :", item_name)
print("Available Stock :", available_stock, "kg")
print("Daily Usage :", daily_usage, "kg")

days_left = available_stock / daily_usage
print("Estimated Days Left :", days_left)

if days_left <= 2:
    print("Inventory Status : CRITICAL")
    print("Advice : Refill immediately")
elif days_left <= 5:
    print("Inventory Status : LOW")
    print("Advice : Plan purchase soon")
else:
    print("Inventory Status : SUFFICIENT")
    print("Advice : No immediate action needed")

# Step 2: Read inputs using function

def household_inventory():
    inventory_records = []

    n = int(input("Enter number of household items : "))

    for i in range(n):
        item = {}

        item["name"] = input("Enter item name : ")
        item["stock"] = float(input("Enter available stock : "))
        item["daily_usage"] = float(input("Enter daily usage : "))
        item["unit"] = input("Enter unit (kg/liters/packets) : ")

        inventory_records.append(item)

    print("\nHousehold Inventory Details")
    for item in inventory_records:
        print("Item Name :", item["name"])
        print("Available Stock :", item["stock"], item["unit"])
        print("Daily Usage :", item["daily_usage"], item["unit"])

        if item["daily_usage"] > 0:
            days_left = item["stock"] / item["daily_usage"]
            print("Estimated Days Left :", days_left)
        else:
            print("Estimated Days Left : Cannot calculate")

        print("--------------------------")

# function call
household_inventory()
# Step 3: Class for Household Inventory Monitor

class HouseholdInventoryMonitor:
    def __init__(self, home_name):
        self.home_name = home_name
        self.inventory_data = []

    def add_item(self, name, stock, daily_usage, unit):
        if stock >= 0 and daily_usage >= 0:
            item = {
                "name": name,
                "stock": stock,
                "daily_usage": daily_usage,
                "unit": unit
            }
            self.inventory_data.append(item)
        else:
            print("Invalid stock or usage value")

    def classify_inventory(self, stock, daily_usage):
        if daily_usage == 0:
            return "No Consumption Data"

        days_left = stock / daily_usage

        if days_left <= 2:
            return "Critical"
        elif days_left <= 5:
            return "Low"
        else:
            return "Sufficient"

    def show_inventory(self):
        print("\nHome Name :", self.home_name)
        print("Inventory Report")

        for item in self.inventory_data:
            status = self.classify_inventory(item["stock"], item["daily_usage"])

            print("Item Name :", item["name"])
            print("Available Stock :", item["stock"], item["unit"])
            print("Daily Usage :", item["daily_usage"], item["unit"])
            print("Inventory Status :", status)

            if item["daily_usage"] > 0:
                print("Estimated Days Left :", item["stock"] / item["daily_usage"])

            print("--------------------------")
# Step 4: Object creation and method call

monitor = HouseholdInventoryMonitor("Ramesh Home")

monitor.add_item("Rice", 10, 2, "kg")
monitor.add_item("Milk", 3, 1, "liters")
monitor.add_item("Sugar", 5, 0.5, "kg")
monitor.add_item("Oil", 1, 0.5, "liters")

monitor.show_inventory()

# Step 5: Intelligent consumption analytics

class SmartConsumptionAnalytics(HouseholdInventoryMonitor):
    def predict_refill(self):
        print("\nRefill Prediction Report")

        for item in self.inventory_data:
            if item["daily_usage"] > 0:
                days_left = item["stock"] / item["daily_usage"]

                print("Item Name :", item["name"])
                print("Predicted Refill Needed In :", days_left, "days")

                if days_left <= 2:
                    print("Recommendation : Buy immediately")
                elif days_left <= 5:
                    print("Recommendation : Add to shopping list")
                else:
                    print("Recommendation : Stock is enough")

                print("--------------------------")

# Step 6: Run smart system

smart_monitor = SmartConsumptionAnalytics("Ramesh Home")

smart_monitor.add_item("Rice", 8, 2, "kg")
smart_monitor.add_item("Milk", 2, 1, "liters")
smart_monitor.add_item("Soap", 6, 0.5, "pieces")
smart_monitor.add_item("Salt", 1, 0.2, "kg")

smart_monitor.show_inventory()
smart_monitor.predict_refill()

class HouseholdInventoryMonitor:
    def __init__(self, home):
        self.home = home
        self.data = []

    def add_item(self, n, s, u, unit):
        if s >= 0 and u >= 0:
            self.data.append({"n": n, "s": s, "u": u, "unit": unit})

    def status(self, s, u):
        if u == 0: return "No Data"
        d = s / u
        return "Critical" if d <= 2 else "Low" if d <= 5 else "Sufficient"

    def show(self):
        print("\nInventory Report -", self.home)
        for i in self.data:
            d = i["s"]/i["u"] if i["u"] else 0
            print(i["n"], "-", self.status(i["s"], i["u"]), "| Days:", d)


class SmartConsumptionAnalytics(HouseholdInventoryMonitor):
    def predict(self):
        print("\nAnalytics Report")
        for i in self.data:
            if i["u"] > 0:
                d = i["s"]/i["u"]
                msg = "Buy Now" if d <= 2 else "Plan Soon" if d <= 5 else "Enough"
                print(i["n"], "-", d, "days ->", msg)


# Run
sys = SmartConsumptionAnalytics("Ramesh Home")

for x in [("Rice",10,2,"kg"), ("Milk",3,1,"liters"),
          ("Sugar",4,0.5,"kg"), ("Oil",2,0.5,"liters")]:
    sys.add_item(*x)

sys.show()
sys.predict()
# object creation
system = SmartConsumptionAnalytics("Ramesh Home")

# adding items
system.add_item("Rice", 10, 2, "kg")
system.add_item("Milk", 3, 1, "liters")
system.add_item("Sugar", 4, 0.5, "kg")
system.add_item("Oil", 2, 0.5, "liters")

# display report
system.show_inventory()

