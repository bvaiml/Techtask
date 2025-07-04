def risk_profiling_engine(applicant_data):
    print("\n[RISK PROFILING ENGINE]")

    age = applicant_data["age"]
    driving = applicant_data["driving_incidents"]
    health = applicant_data["health_score"]

    risk = (0.3 * age / 100) + (0.5 * driving / 5) + (0.2 * (1 - health))

    if risk <= 0.5:
        level = "Low"
    elif risk <= 0.8:
        level = "Medium"
    else:
        level = "High"

    explain = f"Based on age ({age}), driving incidents ({driving}), and health ({health})"
    print(f" Risk Score: {risk:.3f}")
    print(f" Risk Level: {level}")
    print(" Details:", explain)

    return {
        "risk_score": risk,
        "risk_level": level,
        "explanation": explain
    }


def market_conditions_analyzer():
    print("\n[MARKET CONDITIONS ANALYZER]")
    factor = 1.05
    details = "5% adjustment because of claim stats last month"
    print(f" Adjustment Factor: {factor}")
    print(f" Info: {details}")

    return {
        "adjustment_factor": factor,
        "explanation": details
    }


def pricing_optimizer(base, risk_data, market_data):
    print("\n[PRICING OPTIMIZER]")
    multiplier = 1 + risk_data["risk_score"]
    result = base * multiplier * market_data["adjustment_factor"]
    note = (
        f"using risk multiplier ({multiplier:.2f}) "
        f"and market factor ({market_data['adjustment_factor']:.2f})"
    )
    print(f" Final Premium will be: ₹{result:.2f}")
    print(" Notes:", note)
    return {
        "final_premium": round(result, 2),
        "explanation": note
    }


def quote_generator(name, premium_data, risk_data, market_data):
    print("\n[QUOTE SECTION]")
    final = (
        f"\nHi {name},\n\n"
        f"Premium: ₹{premium_data['final_premium']}.\n"
        f"Risk: {risk_data['risk_level']} ({risk_data['risk_score']:.2f})\n"
        f"Risk Info: {risk_data['explanation']}\n"
        f"Market Info: {market_data['explanation']}\n"
        f"Pricing Info: {premium_data['explanation']}\n\n"
        f"Thanks for checking this out."
    )
    print(final)


def main():
    print("Dynamic Insurance Premium Calculator")

    try:
        print("[USER INFO]")
        name = input(" Name: ")
        age = int(input(" Age: "))
        driving = int(input(" Driving incidents in 5 years: "))
        health = float(input(" Health score (0 to 1): "))

        if health < 0 or health > 1:
            raise ValueError("health must be 0 to 1")

        applicant = {
            "name": name,
            "age": age,
            "driving_incidents": driving,
            "health_score": health
        }

        risk = risk_profiling_engine(applicant)
        market = market_conditions_analyzer()
        base_rate = 10000
        premium = pricing_optimizer(base_rate, risk, market)
        quote_generator(name, premium, risk, market)

        print("\nDone.\n")

    except ValueError as ve:
        print("Bad input:", ve)
    except Exception as e:
        print("Something went wrong:", e)


if __name__ == "__main__":
    main()
