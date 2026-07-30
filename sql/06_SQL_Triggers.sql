-- ============================================================
-- Trigger 1: Prevent Negative Inventory Quantity
-- ============================================================
-- Business Purpose:
-- Prevents inventory records from having negative stock
-- quantities during updates.
--
-- Business Benefits:
-- • Maintains inventory accuracy.
-- • Prevents invalid stock records.
-- • Improves reporting reliability.
-- ============================================================

DROP TRIGGER IF EXISTS trg_PreventNegativeInventory;

DELIMITER $$

CREATE TRIGGER trg_PreventNegativeInventory

BEFORE UPDATE
ON Medicines_Inventory

FOR EACH ROW

BEGIN

    IF NEW.Quantity_In_Stock < 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Inventory quantity cannot be negative.';

    END IF;

END $$

DELIMITER ;


-- ============================================================
-- Trigger 2: Auto Update Stock Status
-- ============================================================
-- Business Purpose:
-- Automatically updates stock status whenever inventory
-- quantity changes.
--
-- Business Benefits:
-- • Eliminates manual updates.
-- • Maintains inventory consistency.
-- • Supports inventory monitoring.
-- ============================================================

DROP TRIGGER IF EXISTS trg_UpdateStockStatus;

DELIMITER $$

CREATE TRIGGER trg_UpdateStockStatus

BEFORE UPDATE
ON Medicines_Inventory

FOR EACH ROW

BEGIN

    IF NEW.Quantity_In_Stock = 0 THEN

        SET NEW.Stock_Status = 'Out of Stock';

    ELSEIF NEW.Quantity_In_Stock <= NEW.Reorder_Level THEN

        SET NEW.Stock_Status = 'Low Stock';

    ELSE

        SET NEW.Stock_Status = 'In Stock';

    END IF;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 3: Validate Selling Price
-- ============================================================
-- Business Purpose:
-- Prevents selling price from being less than unit cost.
--
-- Business Benefits:
-- • Prevents financial loss.
-- • Maintains pricing integrity.
-- ============================================================

DROP TRIGGER IF EXISTS trg_ValidateSellingPrice;

DELIMITER $$

CREATE TRIGGER trg_ValidateSellingPrice

BEFORE INSERT
ON Medicines_Inventory

FOR EACH ROW

BEGIN

    IF NEW.Selling_Price < NEW.Unit_Cost THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Selling Price cannot be less than Unit Cost.';

    END IF;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 4: Validate Expiry Date
-- ============================================================

DROP TRIGGER IF EXISTS trg_ValidateExpiryDate;

DELIMITER $$

CREATE TRIGGER trg_ValidateExpiryDate

BEFORE INSERT
ON Medicines_Inventory

FOR EACH ROW

BEGIN

    IF NEW.Expiry_Date <= CURDATE() THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Expiry date must be a future date.';

    END IF;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 5: Prevent Duplicate Batch Number
-- ============================================================

DROP TRIGGER IF EXISTS trg_PreventDuplicateBatch;

DELIMITER $$

CREATE TRIGGER trg_PreventDuplicateBatch

BEFORE INSERT
ON Medicines_Inventory

FOR EACH ROW

BEGIN

    IF EXISTS (

        SELECT 1
        FROM Medicines_Inventory
        WHERE Medicine_ID = NEW.Medicine_ID
        AND Batch_Number = NEW.Batch_Number

    )

    THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Duplicate Batch Number found.';

    END IF;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 6: Auto Calculate Waste Value
-- ============================================================

DROP TRIGGER IF EXISTS trg_CalculateWasteValue;

DELIMITER $$

CREATE TRIGGER trg_CalculateWasteValue

BEFORE INSERT
ON Waste_Records

FOR EACH ROW

BEGIN

    SET NEW.Total_Waste_Value =
    NEW.Quantity_Wasted * NEW.Unit_Cost;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 7: Prevent Future Waste Date
-- ============================================================

DROP TRIGGER IF EXISTS trg_ValidateWasteDate;

DELIMITER $$

CREATE TRIGGER trg_ValidateWasteDate

BEFORE INSERT
ON Waste_Records

FOR EACH ROW

BEGIN

    IF NEW.Waste_Date > CURDATE() THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Waste date cannot be in the future.';

    END IF;

END $$

DELIMITER ;

-- ============================================================
-- Trigger 8: Validate Quantity Sold
-- ============================================================

DROP TRIGGER IF EXISTS trg_ValidateQuantitySold;

DELIMITER $$

CREATE TRIGGER trg_ValidateQuantitySold

BEFORE INSERT
ON Sales_Transactions

FOR EACH ROW

BEGIN

    IF NEW.Quantity_Sold <= 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Quantity Sold must be greater than zero.';

    END IF;

END $$

DELIMITER ;


-- ============================================================
-- Trigger 9: Automatically Reduce Inventory After Sale
-- ============================================================
-- Business Purpose:
-- Automatically deducts the sold quantity from the available
-- inventory whenever a sales transaction is recorded.
--
-- Business Benefits:
-- • Eliminates manual inventory updates.
-- • Maintains real-time stock levels.
-- • Improves inventory accuracy.
-- • Supports pharmacy inventory automation.
-- ============================================================

DROP TRIGGER IF EXISTS trg_UpdateInventoryAfterSale;

DELIMITER $$

CREATE TRIGGER trg_UpdateInventoryAfterSale

AFTER INSERT
ON Sales_Transactions

FOR EACH ROW

BEGIN

    UPDATE Medicines_Inventory

    SET Quantity_In_Stock = Quantity_In_Stock - NEW.Quantity_Sold

    WHERE Medicine_ID = NEW.Medicine_ID

    ORDER BY Expiry_Date ASC

    LIMIT 1;

END $$

DELIMITER ;


-- ============================================================
-- Trigger 10: Prevent Selling More Than Available Stock
-- ============================================================
-- Business Purpose:
-- Prevents sales transactions when the requested quantity
-- exceeds the available inventory.
--
-- Business Benefits:
-- • Prevents negative inventory.
-- • Improves stock accuracy.
-- • Avoids overselling medicines.
-- • Maintains business integrity.
-- ============================================================

DROP TRIGGER IF EXISTS trg_CheckAvailableStock;

DELIMITER $$

CREATE TRIGGER trg_CheckAvailableStock

BEFORE INSERT
ON Sales_Transactions

FOR EACH ROW

BEGIN

    DECLARE v_CurrentStock INT;

    SELECT Quantity_In_Stock

    INTO v_CurrentStock

    FROM Medicines_Inventory

    WHERE Medicine_ID = NEW.Medicine_ID

    ORDER BY Expiry_Date ASC

    LIMIT 1;

    IF v_CurrentStock IS NULL THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Medicine not found in inventory.';

    END IF;

    IF NEW.Quantity_Sold > v_CurrentStock THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock available.';

    END IF;

END $$

DELIMITER ;
