"""ESET module for Get ESET Product Code project"""

def get_product_code (UUID: str) -> str:
    """Returns ESET Product Code generated from UUID"""

    # Check length of UUID, should be 36 characters long with hyphens (32 without hyphens)
    if UUID.__contains__("-"):
        if len(UUID) < 36:
            raise ValueError(f"Not enough characters. 36 expected, {len(UUID)} received.")
        
        if len(UUID) > 36:
            raise ValueError(f"Too many characters. 36 expected, {len(UUID)} received.")
        
        # Remove the hyphens
        UUID = UUID.replace("-","")
    else:
        if len(UUID) < 32:
            raise ValueError(f"Not enough characters. 36 expected, {len(UUID)} received.")
        
        if len(UUID) > 32:
            raise ValueError(f"Too many characters. 36 expected, {len(UUID)} received.")

    # Process UUID to get product code
    # Reverse first 8, next 4, next 4, then 2, 2, 2, 2, 2, 2, 2, then final 2
    product_code = UUID[7]+UUID[6]+UUID[5]+UUID[4]+UUID[3]+UUID[2]+UUID[1]+UUID[0] + UUID[11]+UUID[10]+UUID[9]+UUID[8] + UUID[15]+UUID[14]+UUID[13]+UUID[12] + \
        UUID[17]+UUID[16] + UUID[19]+UUID[18] + UUID[21]+UUID[20] + UUID[23]+UUID[22] + UUID[25]+UUID[24] + UUID[27]+UUID[26] + UUID[29]+ UUID[28] + UUID[31]+UUID[30]

    return product_code

if __name__ == "__main__":
    print(f"\nGet ESET Product Code (eset.py)")
    print("By Patrick Cage (patrick@patrickcage.com)")
    print("This module is intended to be imported by main.py\n")
