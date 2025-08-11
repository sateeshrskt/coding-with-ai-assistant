# LPG Bill Calculator
def get_cylinder_price(cylinder_type):
	prices = {
		"Domestic 14.2 kg": 905.00,
		"Domestic 5 kg": 335.50,
		"Commercial 19 kg": 1886.50,
		"Commercial 47.5 kg": 4712.00
	}
	return prices.get(cylinder_type, 0)

def main():
	print("LPG Bill Calculator")
	cylinder_type = input("Enter Cylinder Type (Domestic 14.2 kg / Domestic 5 kg / Commercial 19 kg / Commercial 47.5 kg): ")
	num_cylinders = int(input("Enter Number of Cylinders Booked: "))
	subsidy = 0.0
	if cylinder_type.startswith("Domestic"):
		subsidy = float(input("Enter Subsidy Amount (if any, else 0): "))
	delivery_charges = float(input("Enter Delivery Charges (₹10 to ₹50): "))

	price_per_cylinder = get_cylinder_price(cylinder_type)
	base_amount = price_per_cylinder * num_cylinders
	bill_amount = base_amount - subsidy + delivery_charges

	print("\n--- Itemized LPG Bill ---")
	print(f"Cylinder Type: {cylinder_type}")
	print(f"Number of Cylinders: {num_cylinders}")
	print(f"Base Amount: ₹{base_amount:.2f}")
	print(f"Subsidy: ₹{subsidy:.2f}")
	print(f"Delivery Charges: ₹{delivery_charges:.2f}")
	print(f"Total Bill Amount: ₹{bill_amount:.2f}")

if __name__ == "__main__":
	main()
