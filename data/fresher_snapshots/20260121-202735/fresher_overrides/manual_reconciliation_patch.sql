-- Manual reconciliation patch (generated)
-- Generated: 2026-01-04T07:46:55
BEGIN TRANSACTION;
DELETE FROM wave_matches;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (1, 3, 'CC_PURCHASE', NULL, 1865, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (2, 6, 'CC_PURCHASE', NULL, 1859, 1581, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (3, 9, 'CC_PURCHASE', NULL, 1846, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (4, 10, 'CC_PURCHASE', NULL, 1806, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_7D', 7, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (5, 14, 'CC_PURCHASE', NULL, 1793, 1608, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (6, 15, 'CC_PURCHASE', NULL, 4153, 1638, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (7, 17, 'CC_PURCHASE', NULL, 1764, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (8, 20, 'CC_PURCHASE', NULL, 1737, 1608, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (9, 21, 'CC_PURCHASE', NULL, 1734, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_5D', 5, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (10, 23, 'CC_PURCHASE', NULL, 4152, 1638, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (11, 26, 'CC_PURCHASE', NULL, 1730, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (12, 27, 'CC_PURCHASE', NULL, 1728, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (13, 28, 'CC_PURCHASE', NULL, 1727, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_1D', -1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (14, 29, 'CC_PURCHASE', NULL, 4149, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (15, 30, 'CC_PURCHASE', NULL, 1671, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (16, 32, 'CC_PURCHASE', NULL, 1663, 1608, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (17, 33, 'CC_PURCHASE', NULL, 1665, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (18, 37, 'CC_PURCHASE', NULL, 1657, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (19, 38, 'CC_PURCHASE', NULL, 1658, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (20, 40, 'CC_PURCHASE', NULL, 1644, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (21, 41, 'CC_PURCHASE', NULL, 4123, 1637, 'HIGH', 'CC_PURCHASE_VENDOR_21D', 21, 0, 'Card 8154 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (22, 44, 'CC_PURCHASE', NULL, 1646, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (23, 45, 'CC_PURCHASE', NULL, 4143, 1642, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (24, 46, 'CC_PURCHASE', NULL, 4144, 1638, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (25, 47, 'CC_PURCHASE', NULL, 1645, 1570, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (26, 51, 'CC_PURCHASE', NULL, 1631, 1608, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (27, 52, 'CC_PURCHASE', NULL, 1628, 1608, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (28, 54, 'CC_PURCHASE', NULL, 1626, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (29, 58, 'CC_PURCHASE', NULL, 1624, 1608, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (30, 60, 'CC_PURCHASE', NULL, 1619, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (31, 61, 'CC_PURCHASE', NULL, 4135, 1642, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (32, 66, 'CC_PURCHASE', NULL, 4132, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (33, 68, 'CC_PURCHASE', NULL, 4133, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (34, 69, 'CC_PURCHASE', NULL, 4131, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (35, 71, 'CC_PURCHASE', NULL, 4121, 1638, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (36, 76, 'CC_PURCHASE', NULL, 1583, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (37, 77, 'CC_PURCHASE', NULL, 1581, 1604, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (38, 80, 'CC_PURCHASE', NULL, 4101, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (39, 83, 'CC_PURCHASE', NULL, 4100, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (40, 85, 'CC_PURCHASE', NULL, 4098, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (41, 88, 'CC_PURCHASE', NULL, 4096, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (42, 89, 'CC_PURCHASE', NULL, 4095, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (43, 90, 'CC_PURCHASE', NULL, 4082, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_9D', 9, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (44, 91, 'CC_PURCHASE', NULL, 4094, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (45, 92, 'CC_PURCHASE', NULL, 4093, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (46, 97, 'CC_PURCHASE', NULL, 1553, 1608, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (47, 98, 'CC_PURCHASE', NULL, 4080, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (48, 100, 'CC_PURCHASE', NULL, 4081, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (49, 102, 'CC_PURCHASE', NULL, 1524, 1557, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (50, 103, 'CC_PURCHASE', NULL, 1523, 1557, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (51, 108, 'CC_PURCHASE', NULL, 4058, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (52, 112, 'CC_PURCHASE', NULL, 4053, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (53, 113, 'CC_PURCHASE', NULL, 4051, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (54, 114, 'CC_PURCHASE', NULL, 4052, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (55, 118, 'CC_PURCHASE', NULL, 1485, 1530, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (56, 119, 'CC_PURCHASE', NULL, 1484, 1529, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (57, 120, 'CC_PURCHASE', NULL, 1481, 1530, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (58, 123, 'CC_PURCHASE', NULL, 1471, 1517, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (59, 124, 'CC_PURCHASE', NULL, 4047, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (60, 128, 'CC_PURCHASE', NULL, 4033, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (61, 133, 'CC_PURCHASE', NULL, 1436, 1489, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (62, 134, 'CC_PURCHASE', NULL, 4004, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (63, 135, 'CC_PURCHASE', NULL, 4000, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (64, 138, 'CC_PURCHASE', NULL, 3992, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (65, 139, 'CC_PURCHASE', NULL, 3985, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (66, 140, 'CC_PURCHASE', NULL, 1416, 1459, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (67, 143, 'CC_PURCHASE', NULL, 3973, 1437, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (68, 157, 'CC_PURCHASE', NULL, 3922, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (69, 158, 'CC_PURCHASE', NULL, 1360, 1337, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (70, 160, 'CC_PURCHASE', NULL, 1362, 1096, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match] | Paid via bank transfer 1096 (2024-05-28).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (71, 161, 'CC_PURCHASE', NULL, 3919, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (72, 162, 'CC_PURCHASE', NULL, 1358, 1398, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (73, 163, 'CC_PURCHASE', NULL, 1356, 1402, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (74, 167, 'CC_PURCHASE', NULL, 1343, 1368, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (75, 168, 'CC_PURCHASE', NULL, 3899, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (76, 169, 'CC_PURCHASE', NULL, 3898, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (77, 170, 'CC_PURCHASE', NULL, 1340, 1368, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (78, 173, 'CC_PURCHASE', NULL, 1337, 1368, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (79, 174, 'CC_PURCHASE', NULL, 1336, 1368, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (80, 175, 'CC_PURCHASE', NULL, 1344, 1368, 'HIGH', 'CC_PURCHASE_VENDOR_5D', -5, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (81, 177, 'CC_PURCHASE', NULL, 1322, 1343, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (82, 178, 'CC_PURCHASE', NULL, 1325, 1336, 'HIGH', 'CC_PURCHASE_AMOUNT_0D', 0, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (83, 179, 'CC_PURCHASE', NULL, 3887, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (84, 180, 'CC_PURCHASE', NULL, 1316, 1343, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (85, 181, 'CC_PURCHASE', NULL, 1317, 1343, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (86, 183, 'CC_PURCHASE', NULL, 1311, 1333, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (87, 184, 'CC_PURCHASE', NULL, 1310, 1343, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (88, 186, 'CC_PURCHASE', NULL, 1312, 1343, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (89, 189, 'CC_PURCHASE', NULL, 3874, 1335, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (90, 190, 'CC_PURCHASE', NULL, 3868, 1318, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 8154 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (91, 192, 'CC_PURCHASE', NULL, 1295, 1325, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (92, 194, 'CC_PURCHASE', NULL, 1292, 1326, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (93, 197, 'CC_PURCHASE', NULL, 3863, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (94, 200, 'CC_PURCHASE', NULL, 1283, 1288, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (95, 201, 'CC_PURCHASE', NULL, 1277, 1289, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (96, 202, 'CC_PURCHASE', NULL, 1280, 1288, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (97, 203, 'CC_PURCHASE', NULL, 1274, 1288, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (98, 206, 'CC_PURCHASE', NULL, 1267, 1302, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (99, 208, 'CC_PURCHASE', NULL, 1268, 1289, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (100, 210, 'CC_PURCHASE', NULL, 3852, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (101, 211, 'CC_PURCHASE', NULL, 1264, 1289, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (102, 217, 'CC_PURCHASE', NULL, 1259, 1289, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (103, 218, 'CC_PURCHASE', NULL, 1258, 1302, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (104, 219, 'CC_PURCHASE', NULL, 1256, 1288, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (105, 226, 'CC_PURCHASE', NULL, 3839, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (106, 227, 'CC_PURCHASE', NULL, 1239, 1270, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (107, 228, 'CC_PURCHASE', NULL, 1240, 1270, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (108, 229, 'CC_PURCHASE', NULL, 1235, 1270, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (109, 231, 'CC_PURCHASE', NULL, 3829, 1268, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (110, 234, 'CC_PURCHASE', NULL, 1219, 1250, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (111, 236, 'CC_PURCHASE', NULL, 1218, 1249, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (112, 238, 'CC_PURCHASE', NULL, 1214, 1250, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (113, 242, 'CC_PURCHASE', NULL, 3814, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (114, 244, 'CC_PURCHASE', NULL, 3808, 1219, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (115, 248, 'CC_PURCHASE', NULL, 1205, 1235, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (116, 255, 'CC_PURCHASE', NULL, 3805, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (117, 256, 'CC_PURCHASE', NULL, 3802, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (118, 260, 'CC_PURCHASE', NULL, 3797, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (119, 261, 'CC_PURCHASE', NULL, 1190, 1206, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (120, 262, 'CC_PURCHASE', NULL, 1189, 1206, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (121, 264, 'CC_PURCHASE', NULL, 1188, 1204, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (122, 265, 'CC_PURCHASE', NULL, 1187, 1206, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (123, 267, 'CC_PURCHASE', NULL, 1179, 1204, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (124, 268, 'CC_PURCHASE', NULL, 3782, 1195, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (125, 270, 'CC_PURCHASE', NULL, 1174, 1193, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (126, 271, 'CC_PURCHASE', NULL, 1170, 1194, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (127, 279, 'CC_PURCHASE', NULL, 3761, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (128, 282, 'CC_PURCHASE', NULL, 3756, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (129, 283, 'CC_PURCHASE', NULL, 3757, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (131, 285, 'CC_PURCHASE', NULL, 3755, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (132, 287, 'CC_PURCHASE', NULL, 3751, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (133, 288, 'CC_PURCHASE', NULL, 3749, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (134, 289, 'CC_PURCHASE', NULL, 3742, 1157, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (135, 290, 'CC_PURCHASE', NULL, 3744, 1155, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (136, 292, 'CC_PURCHASE', NULL, 1143, 1144, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (137, 293, 'CC_PURCHASE', NULL, 1144, 1144, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (138, 294, 'CC_PURCHASE', NULL, 1140, 1147, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (139, 295, 'CC_PURCHASE', NULL, 1141, 1144, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (140, 298, 'CC_PURCHASE', NULL, 1124, 1135, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (141, 299, 'CC_PURCHASE', NULL, 1125, 1135, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (142, 300, 'CC_PURCHASE', NULL, 1123, 1135, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (143, 302, 'CC_PURCHASE', NULL, 1114, 1096, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (144, 306, 'CC_PURCHASE', NULL, 1095, 1118, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (145, 307, 'CC_PURCHASE', NULL, 1094, 1118, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (146, 308, 'CC_PURCHASE', NULL, 1093, 1118, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (147, 309, 'CC_PURCHASE', NULL, 1086, 1115, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (148, 311, 'CC_PURCHASE', NULL, 3695, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (149, 315, 'CC_PURCHASE', NULL, 1059, 1102, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (150, 316, 'CC_PURCHASE', NULL, 1036, 1097, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (151, 318, 'CC_PURCHASE', NULL, 1025, 1093, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (152, 319, 'CC_PURCHASE', NULL, 1024, 1094, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (153, 325, 'CC_PURCHASE', NULL, 962, 1079, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (154, 329, 'CC_PURCHASE', NULL, 916, 1072, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (155, 331, 'CC_PURCHASE', NULL, 913, 1072, 'HIGH', 'CC_PURCHASE_AMOUNT_0D', 0, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (156, 333, 'CC_PURCHASE', NULL, 3551, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (157, 335, 'CC_PURCHASE', NULL, 879, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (158, 337, 'CC_PURCHASE', NULL, 872, 1054, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (159, 340, 'CC_PURCHASE', NULL, 3533, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (160, 348, 'CC_PURCHASE', NULL, 3524, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (161, 350, 'CC_PURCHASE', NULL, 3519, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (162, 354, 'CC_PURCHASE', NULL, 3515, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (163, 356, 'CC_PURCHASE', NULL, 3510, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (164, 357, 'CC_PURCHASE', NULL, 3507, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (165, 359, 'CC_PURCHASE', NULL, 3506, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (166, 360, 'CC_PURCHASE', NULL, 856, 1023, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (167, 361, 'CC_PURCHASE', NULL, 3505, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (168, 367, 'CC_PURCHASE', NULL, 3486, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (169, 368, 'CC_PURCHASE', NULL, 3485, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (170, 378, 'CC_PURCHASE', NULL, 3477, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (171, 380, 'CC_PURCHASE', NULL, 3475, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (172, 384, 'CC_PURCHASE', NULL, 3473, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (173, 387, 'CC_PURCHASE', NULL, 3471, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (174, 388, 'CC_PURCHASE', NULL, 3467, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (175, 395, 'CC_PURCHASE', NULL, 3458, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (176, 401, 'CC_PURCHASE', NULL, 3470, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_5D', -5, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (177, 405, 'CC_PURCHASE', NULL, 3439, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (178, 406, 'CC_PURCHASE', NULL, 3430, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (179, 407, 'CC_PURCHASE', NULL, 3434, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (180, 408, 'CC_PURCHASE', NULL, 3432, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (181, 413, 'CC_PURCHASE', NULL, 3417, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (182, 415, 'CC_PURCHASE', NULL, 3415, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (183, 416, 'CC_PURCHASE', NULL, 813, 952, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (184, 422, 'CC_PURCHASE', NULL, 808, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (186, 426, 'CC_PURCHASE', NULL, 3407, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (187, 427, 'CC_PURCHASE', NULL, 3402, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (188, 432, 'CC_PURCHASE', NULL, 3399, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (189, 436, 'CC_PURCHASE', NULL, 3391, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (190, 440, 'CC_PURCHASE', NULL, 779, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (191, 441, 'CC_PURCHASE', NULL, 3387, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (192, 444, 'CC_PURCHASE', NULL, 781, 889, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (193, 446, 'CC_PURCHASE', NULL, 3382, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (194, 451, 'CC_PURCHASE', NULL, 3384, NULL, 'EXACT', 'CC_PURCHASE_VENDOR_0D', 0, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (195, 454, 'CC_PURCHASE', NULL, 3374, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (196, 456, 'CC_PURCHASE', NULL, 3369, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (197, 458, 'CC_PURCHASE', NULL, 775, 873, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (198, 464, 'CC_PURCHASE', NULL, 3361, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (199, 466, 'CC_PURCHASE', NULL, 755, 841, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (200, 469, 'CC_PURCHASE', NULL, 3357, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (201, 470, 'CC_PURCHASE', NULL, 3356, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (202, 473, 'CC_PURCHASE', NULL, 3355, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (203, 477, 'CC_PURCHASE', NULL, 3349, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (204, 478, 'CC_PURCHASE', NULL, 3347, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (205, 480, 'CC_PURCHASE', NULL, 3341, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (206, 483, 'CC_PURCHASE', NULL, 3330, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (207, 488, 'CC_PURCHASE', NULL, 3327, 771, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (208, 489, 'CC_PURCHASE', NULL, 732, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (209, 491, 'CC_PURCHASE', NULL, 3323, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (210, 492, 'CC_PURCHASE', NULL, 3321, 771, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (211, 494, 'CC_PURCHASE', NULL, 3320, 771, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 8154 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (212, 496, 'CC_PURCHASE', NULL, 728, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (213, 499, 'CC_PURCHASE', NULL, 3306, 775, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (214, 500, 'CC_PURCHASE', NULL, 3309, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (215, 508, 'CC_PURCHASE', NULL, 3280, 753, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 8154 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (216, 511, 'CC_PURCHASE', NULL, 3290, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (217, 515, 'CC_PURCHASE', NULL, 3279, 753, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (218, 519, 'CC_PURCHASE', NULL, 3275, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (219, 524, 'CC_PURCHASE', NULL, 707, 740, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (220, 527, 'CC_PURCHASE', NULL, 3251, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (221, 532, 'CC_PURCHASE', NULL, 3248, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (222, 533, 'CC_PURCHASE', NULL, 3237, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (223, 535, 'CC_PURCHASE', NULL, 3218, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (224, 545, 'CC_PURCHASE', NULL, 3182, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (225, 549, 'CC_PURCHASE', NULL, 3176, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (226, 550, 'CC_PURCHASE', NULL, 683, 679, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (227, 551, 'CC_PURCHASE', NULL, 3172, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (228, 552, 'CC_PURCHASE', NULL, 3174, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (229, 553, 'CC_PURCHASE', NULL, 3173, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (230, 558, 'CC_PURCHASE', NULL, 3158, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (231, 559, 'CC_PURCHASE', NULL, 3159, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (232, 564, 'CC_PURCHASE', NULL, 3154, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (233, 565, 'CC_PURCHASE', NULL, 3153, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (234, 566, 'CC_PURCHASE', NULL, 3152, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (235, 567, 'CC_PURCHASE', NULL, 668, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (236, 568, 'CC_PURCHASE', NULL, 3151, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (237, 569, 'CC_PURCHASE', NULL, 3150, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (238, 570, 'CC_PURCHASE', NULL, 664, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (239, 571, 'CC_PURCHASE', NULL, 665, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (240, 577, 'CC_PURCHASE', NULL, 3130, 610, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (241, 578, 'CC_PURCHASE', NULL, 3128, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (242, 579, 'CC_PURCHASE', NULL, 3124, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (243, 580, 'CC_PURCHASE', NULL, 3125, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (244, 581, 'CC_PURCHASE', NULL, 3127, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (245, 582, 'CC_PURCHASE', NULL, 656, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (246, 586, 'CC_PURCHASE', NULL, 3112, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (247, 587, 'CC_PURCHASE', NULL, 647, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (248, 588, 'CC_PURCHASE', NULL, 645, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (249, 590, 'CC_PURCHASE', NULL, 641, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (250, 591, 'CC_PURCHASE', NULL, 643, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (251, 592, 'CC_PURCHASE', NULL, 632, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (252, 594, 'CC_PURCHASE', NULL, 623, 576, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (253, 596, 'CC_PURCHASE', NULL, 607, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (254, 598, 'CC_PURCHASE', NULL, 604, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (255, 600, 'CC_PURCHASE', NULL, 3087, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (256, 601, 'CC_PURCHASE', NULL, 3086, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (257, 603, 'CC_PURCHASE', NULL, 3085, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (258, 604, 'CC_PURCHASE', NULL, 598, 555, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (259, 606, 'CC_PURCHASE', NULL, 593, 555, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (260, 607, 'CC_PURCHASE', NULL, 592, 555, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (261, 608, 'CC_PURCHASE', NULL, 594, 576, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (262, 609, 'CC_PURCHASE', NULL, 567, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_7D', 7, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (263, 613, 'CC_PURCHASE', NULL, 3066, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (264, 614, 'CC_PURCHASE', NULL, 570, 562, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (265, 617, 'CC_PURCHASE', NULL, 569, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (266, 618, 'CC_PURCHASE', NULL, 3060, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 7022 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (267, 620, 'CC_PURCHASE', NULL, 566, 516, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (268, 621, 'CC_PURCHASE', NULL, 564, 516, 'HIGH', 'CC_PURCHASE_AMOUNT_3D', 3, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (269, 623, 'CC_PURCHASE', NULL, 556, 516, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (270, 626, 'CC_PURCHASE', NULL, 551, NULL, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 4337 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (271, 629, 'CC_PURCHASE', NULL, 3040, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (272, 633, 'CC_PURCHASE', NULL, 539, 516, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (273, 634, 'CC_PURCHASE', NULL, 3034, 519, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (274, 641, 'CC_PURCHASE', NULL, 516, 459, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (275, 642, 'CC_PURCHASE', NULL, 513, 472, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (276, 643, 'CC_PURCHASE', NULL, 515, 462, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (277, 644, 'CC_PURCHASE', NULL, 512, 459, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (278, 647, 'CC_PURCHASE', NULL, 3003, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (279, 653, 'CC_PURCHASE', NULL, 503, 462, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (280, 655, 'CC_PURCHASE', NULL, 501, 459, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (281, 656, 'CC_PURCHASE', NULL, 500, 462, 'HIGH', 'CC_PURCHASE_VENDOR_2D', 2, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (282, 657, 'CC_PURCHASE', NULL, 482, 453, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (283, 658, 'CC_PURCHASE', NULL, 478, 442, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (284, 659, 'CC_PURCHASE', NULL, 481, 453, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (285, 663, 'CC_PURCHASE', NULL, 474, 442, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (286, 664, 'CC_PURCHASE', NULL, 2983, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 7022');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (287, 665, 'CC_PURCHASE', NULL, 463, 393, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (288, 666, 'CC_PURCHASE', NULL, 468, 450, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (289, 667, 'CC_PURCHASE', NULL, 467, 449, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (290, 669, 'CC_PURCHASE', NULL, 460, 429, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (291, 670, 'CC_PURCHASE', NULL, 462, 431, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (292, 671, 'CC_PURCHASE', NULL, 461, 428, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (293, 673, 'CC_PURCHASE', NULL, 457, 429, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (294, 675, 'CC_PURCHASE', NULL, 456, 428, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (295, 681, 'CC_PURCHASE', NULL, 440, 404, 'HIGH', 'CC_PURCHASE_AMOUNT_4D', 4, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (296, 683, 'CC_PURCHASE', NULL, 433, 404, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (297, 687, 'CC_PURCHASE', NULL, 416, 366, 'HIGH', 'CC_PURCHASE_VENDOR_1D', 1, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (298, 689, 'CC_PURCHASE', NULL, 409, 368, 'HIGH', 'CC_PURCHASE_AMOUNT_2D', 2, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (299, 690, 'CC_PURCHASE', NULL, 408, 368, 'HIGH', 'CC_PURCHASE_VENDOR_3D', 3, 0, 'Card 0318');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (301, 692, 'CC_PURCHASE', NULL, 400, NULL, 'HIGH', 'CC_PURCHASE_VENDOR_4D', 4, 0, 'Card 4337');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (302, 699, 'CC_PURCHASE', NULL, 375, 334, 'HIGH', 'CC_PURCHASE_VENDOR_6D', 6, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (303, 700, 'CC_PURCHASE', NULL, 381, 317, 'HIGH', 'CC_PURCHASE_AMOUNT_1D', 1, 0, 'Card 0318 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (304, 16, 'BANK_DEBIT', 1686, NULL, NULL, 'EXACT', 'BANK_DEBIT_CARD_0D', 0, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (305, 34, 'BANK_DEBIT', 1672, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_10D', 10, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (306, 65, 'BANK_DEBIT', 1649, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_1D', 1, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (307, 67, 'BANK_DEBIT', 1648, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_1D', 1, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (308, 74, 'BANK_DEBIT', 1620, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_9D', 9, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (309, 130, 'BILL_PAYMENT', 1470, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_14D', 14, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (310, 196, 'BILL_PAYMENT', 1317, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (311, 199, 'BILL_PAYMENT', 1316, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (312, 205, 'BILL_PAYMENT', 1290, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_8D', 8, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (313, 212, 'BILL_PAYMENT', 1297, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (314, 213, 'BILL_PAYMENT', 1294, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (315, 214, 'BILL_PAYMENT', 1296, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (316, 215, 'BILL_PAYMENT', 1301, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (317, 225, 'BILL_PAYMENT', 1273, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (318, 237, 'BILL_PAYMENT', 1247, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (319, 241, 'BILL_PAYMENT', 1251, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (320, 247, 'BILL_PAYMENT', 1234, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (321, 257, 'BILL_PAYMENT', 1218, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (322, 269, 'BILL_PAYMENT', 1190, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (323, 273, 'BILL_PAYMENT', 1189, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (324, 332, 'BILL_PAYMENT', 1069, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (325, 341, 'BILL_PAYMENT', 1055, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (326, 343, 'BILL_PAYMENT', 1058, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (327, 353, 'BILL_PAYMENT', 1048, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (328, 355, 'BILL_PAYMENT', 1038, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (329, 362, 'BILL_PAYMENT', 1041, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (330, 370, 'BILL_PAYMENT', 1019, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (331, 372, 'BILL_PAYMENT', 1013, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (332, 373, 'BILL_PAYMENT', 1015, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (333, 376, 'BILL_PAYMENT', 1012, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (334, 377, 'BILL_PAYMENT', 1014, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (335, 379, 'BILL_PAYMENT', 1008, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (336, 381, 'BILL_PAYMENT', 976, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_9D', 9, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (337, 389, 'BILL_PAYMENT', 915, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_27D', 27, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (338, 390, 'BILL_PAYMENT', 916, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_27D', 27, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (339, 391, 'BILL_PAYMENT', 910, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_27D', 27, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (340, 394, 'BANK_DEBIT', 992, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_3D', 3, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (341, 396, 'BILL_PAYMENT', 984, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (342, 397, 'BILL_PAYMENT', 981, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (343, 400, 'BANK_DEBIT', 933, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_16D', 16, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (344, 404, 'BILL_PAYMENT', 914, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_19D', 19, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (345, 409, 'BILL_PAYMENT', 970, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (346, 410, 'BILL_PAYMENT', 969, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (347, 414, 'BILL_PAYMENT', 943, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (348, 419, 'BILL_PAYMENT', 942, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (349, 421, 'BILL_PAYMENT', 944, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (350, 428, 'BILL_PAYMENT', 905, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (351, 430, 'BILL_PAYMENT', 922, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (352, 431, 'BILL_PAYMENT', 923, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (353, 434, 'BILL_PAYMENT', 864, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_13D', 13, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (354, 437, 'BILL_PAYMENT', 904, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (355, 439, 'BANK_DEBIT', 902, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_1D', 1, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (356, 443, 'BILL_PAYMENT', 893, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (357, 445, 'BILL_PAYMENT', 888, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (358, 448, 'BILL_PAYMENT', 890, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (359, 453, 'BILL_PAYMENT', 876, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (360, 457, 'BILL_PAYMENT', 875, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (361, 461, 'BILL_PAYMENT', 860, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (362, 467, 'BILL_PAYMENT', 848, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (363, 468, 'BILL_PAYMENT', 847, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (364, 476, 'BILL_PAYMENT', 819, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (365, 481, 'BILL_PAYMENT', 820, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (366, 487, 'BILL_PAYMENT', 742, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_19D', 19, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (367, 498, 'BILL_PAYMENT', 776, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (368, 513, 'BILL_PAYMENT', 755, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_5D', 5, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (369, 516, 'BILL_PAYMENT', 743, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (370, 526, 'BILL_PAYMENT', 725, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (371, 528, 'BILL_PAYMENT', 730, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_4D', 4, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (372, 530, 'BILL_PAYMENT', 668, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_27D', 27, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (373, 531, 'BILL_PAYMENT', 727, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (374, 534, 'BILL_PAYMENT', 728, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (375, 536, 'BILL_PAYMENT', 700, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_14D', 14, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (376, 538, 'BILL_PAYMENT', 712, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (377, 554, 'BILL_PAYMENT', 682, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_2D', 2, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (378, 557, 'BILL_PAYMENT', 651, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_7D', 7, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (379, 576, 'BILL_PAYMENT', 604, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_10D', 10, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (380, 583, 'BILL_PAYMENT', 607, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (382, 593, 'BILL_PAYMENT', 566, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_15D', 15, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (383, 597, 'BANK_DEBIT', 534, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_23D', 23, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (384, 602, 'BILL_PAYMENT', 561, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_7D', 7, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (385, 611, 'BILL_PAYMENT', 563, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (386, 624, 'BILL_PAYMENT', 522, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_6D', 6, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (387, 630, 'BANK_DEBIT', 517, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_2D', 2, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (388, 632, 'BANK_DEBIT', 530, NULL, NULL, 'EXACT', 'BANK_DEBIT_CARD_0D', 0, 0, 'DEBIT_CARD');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (389, 637, 'BILL_PAYMENT', 474, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_17D', 17, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (390, 640, 'BILL_PAYMENT', 473, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_10D', 10, 1, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (391, 646, 'BILL_PAYMENT', 467, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_8D', 8, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (392, 652, 'BILL_PAYMENT', 465, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (393, 662, 'BILL_PAYMENT', 445, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_1D', 1, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (394, 677, 'BILL_PAYMENT', 403, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_7D', 7, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (395, 680, 'BANK_DEBIT', 398, NULL, NULL, 'HIGH', 'BANK_DEBIT_CARD_10D', 10, 0, 'DEBIT_CARD [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (396, 682, 'BILL_PAYMENT', 405, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_0D', 0, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (397, 684, 'BILL_PAYMENT', 367, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_13D', 13, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (398, 688, 'BILL_PAYMENT', 370, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_3D', 3, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (399, 702, 'BILL_PAYMENT', 333, NULL, NULL, 'HIGH', 'BANK_BILL_PAYMENT_15D', 15, 0, 'BILL_PAYMENT [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (400, 59, 'VENDOR_ETRANSFER', 1656, NULL, NULL, 'HIGH', 'VENDOR_ETRANSFER_1D', 1, 0, 'To COVERED BRIDGE');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (401, 104, 'SHAREHOLDER_REIMBURSE', 1559, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_1D', 1, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (402, 121, 'INTERCOMPANY_PURCHASE', 1521, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_1D', 1, 1, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (403, 136, 'SHAREHOLDER_REIMBURSE', 1492, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_7D', -7, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (404, 165, 'INTERCOMPANY_PURCHASE', 1396, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (405, 187, 'SHAREHOLDER_REIMBURSE', 1351, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_2D', -2, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (406, 195, 'SHAREHOLDER_REIMBURSE', 1324, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (407, 207, 'SHAREHOLDER_REIMBURSE', 1286, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_7D', 7, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (408, 221, 'SHAREHOLDER_REIMBURSE', 1287, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_2D', 2, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (409, 223, 'INTERCOMPANY_PURCHASE', 1284, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (410, 235, 'SHAREHOLDER_REIMBURSE', 1225, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_11D', 11, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (411, 250, 'INTERCOMPANY_PURCHASE', 1243, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_4D', -4, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (412, 251, 'INTERCOMPANY_PURCHASE', 1224, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (413, 252, 'INTERCOMPANY_PURCHASE', 1223, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (414, 301, 'INTERCOMPANY_PURCHASE', 1131, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 3, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (415, 314, 'SHAREHOLDER_REIMBURSE', 1109, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (416, 344, 'SHAREHOLDER_REIMBURSE', 1057, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_4D', 4, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (417, 347, 'SHAREHOLDER_REIMBURSE', 1052, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_1D', 1, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (418, 349, 'INTERCOMPANY_PURCHASE', 1059, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (419, 411, 'SHAREHOLDER_REIMBURSE', 953, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_4D', 4, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (420, 417, 'INTERCOMPANY_PURCHASE', 954, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (421, 442, 'INTERCOMPANY_PURCHASE', 903, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (422, 450, 'INTERCOMPANY_PURCHASE', 894, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (423, 490, 'SHAREHOLDER_REIMBURSE', 781, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_10D', 10, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (424, 493, 'SHAREHOLDER_REIMBURSE', 785, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_9D', 9, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (425, 506, 'INTERCOMPANY_PURCHASE', 790, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (426, 507, 'INTERCOMPANY_PURCHASE', 787, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (427, 555, 'INTERCOMPANY_PURCHASE', 684, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_1D', 1, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (428, 635, 'INTERCOMPANY_PURCHASE', 515, NULL, NULL, 'HIGH', 'SHAREHOLDER_ET_0D', 0, 0, 'To DWAYNE RIPLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (429, 70, 'E_TRANSFER_REIMBURSE', 1645, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_0D', 0, 0, 'To DANIEL GIONET - MONDOUX');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (430, 110, 'E_TRANSFER_REIMBURSE', 1542, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_1D', 1, 0, 'To SNAXIES');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (431, 111, 'E_TRANSFER_REIMBURSE', 1478, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_30D', 30, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (432, 145, 'E_TRANSFER_REIMBURSE', 1447, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_0D', 0, 0, 'To DANIEL GIONET - MONDOUX');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (433, 276, 'E_TRANSFER_REIMBURSE', 1148, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_15D', 15, 0, 'To THOMAS MCCROSSIN [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (434, 328, 'E_TRANSFER_REIMBURSE', 1074, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_5D', 5, 0, 'To DENISE MANLEY');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (435, 495, 'E_TRANSFER_REIMBURSE', 782, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_9D', 9, 0, 'To ONE-TIME CONTACT KYLE MAC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (436, 525, 'E_TRANSFER_REIMBURSE', 683, NULL, NULL, 'HIGH', 'E_TRANSFER_REIMBURSE_27D', 27, 0, 'To DWAYNE RIPLEY [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (437, 36, 'PAD_INVOICE', 1665, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2023-09-15 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (438, 43, 'PAD_INVOICE', 1651, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2023-09-22 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (439, 48, 'PAD_INVOICE', 1634, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2023-09-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (440, 55, 'PAD_INVOICE', 1634, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2023-09-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (441, 56, 'PAD_INVOICE', 1634, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2023-09-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (442, 62, 'PAD_INVOICE', 1623, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2023-10-06 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (443, 63, 'PAD_INVOICE', 1623, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2023-10-06 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (444, 73, 'PAD_INVOICE', 1614, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2023-10-13 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (445, 79, 'PAD_INVOICE', 1600, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2023-10-20 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (446, 87, 'PAD_INVOICE', 1553, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2023-10-27 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (447, 96, 'PAD_INVOICE', 1528, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2023-11-03 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (448, 105, 'PAD_INVOICE', 1513, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 16, 0, 'PAD 2023-11-10 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (449, 107, 'PAD_INVOICE', 1513, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 15, 0, 'PAD 2023-11-10 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (450, 109, 'PAD_INVOICE', 1513, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2023-11-10 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (451, 115, 'PAD_INVOICE', 1500, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 15, 0, 'PAD 2023-11-17 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (452, 116, 'PAD_INVOICE', 1500, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2023-11-17 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (453, 117, 'PAD_INVOICE', 1500, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2023-11-17 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (454, 122, 'PAD_INVOICE', 1491, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 16, 0, 'PAD 2023-11-24 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (455, 127, 'PAD_INVOICE', 1468, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2023-12-01 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (456, 129, 'PAD_INVOICE', 1468, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2023-12-01 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (457, 132, 'PAD_INVOICE', 1454, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2023-12-08 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (458, 137, 'PAD_INVOICE', 1441, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2023-12-15 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (459, 141, 'PAD_INVOICE', 1433, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2023-12-22 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (460, 142, 'PAD_INVOICE', 1433, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2023-12-22 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (461, 146, 'PAD_INVOICE', 1420, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 17, 0, 'PAD 2023-12-29 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (462, 147, 'PAD_INVOICE', 1420, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2023-12-29 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (463, 150, 'PAD_INVOICE', 1384, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2024-01-12 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (464, 159, 'PAD_INVOICE', 1374, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2024-01-19 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (465, 164, 'PAD_INVOICE', 1357, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 18, 0, 'PAD 2024-01-26 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (466, 171, 'PAD_INVOICE', 1331, NULL, NULL, 'HIGH', 'PAD_GFS_SUBSET_1', 15, 10, 'PAD 2024-02-02 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (467, 188, 'PAD_INVOICE', 1309, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2024-02-16 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (468, 193, 'PAD_INVOICE', 1282, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 16, 0, 'PAD 2024-02-23 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (469, 198, 'PAD_INVOICE', 1282, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-02-23 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (470, 204, 'PAD_INVOICE', 1262, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 18, 0, 'PAD 2024-03-01 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (471, 233, 'PAD_INVOICE', 1214, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2024-03-15 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (472, 243, 'PAD_INVOICE', 1201, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2024-03-22 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (473, 245, 'PAD_INVOICE', 1201, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-03-22 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (474, 249, 'PAD_INVOICE', 1181, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 21, 0, 'PAD 2024-04-01 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (475, 253, 'PAD_INVOICE', 1181, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 19, 0, 'PAD 2024-04-01 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (476, 254, 'PAD_INVOICE', 1181, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 19, 0, 'PAD 2024-04-01 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (477, 263, 'PAD_INVOICE', 1181, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 17, 0, 'PAD 2024-04-01 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (478, 286, 'PAD_INVOICE', 1125, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 18, 0, 'PAD 2024-04-26 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (479, 291, 'PAD_INVOICE', 1125, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2024-04-26 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (480, 297, 'PAD_INVOICE', 1121, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2024-05-03 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (481, 304, 'PAD_INVOICE', 1105, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-05-17 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (482, 305, 'PAD_INVOICE', 1105, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-05-17 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (483, 313, 'PAD_INVOICE', 1099, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2024-05-24 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (484, 320, 'PAD_INVOICE', 1083, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2024-06-21 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (485, 330, 'PAD_INVOICE', 1065, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 16, 0, 'PAD 2024-08-23 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (486, 342, 'PAD_INVOICE', 1031, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2024-09-13 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (487, 351, 'PAD_INVOICE', 1011, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 16, 0, 'PAD 2024-09-20 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (488, 352, 'PAD_INVOICE', 1011, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2024-09-20 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (489, 358, 'PAD_INVOICE', 994, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 19, 0, 'PAD 2024-09-27 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (490, 363, 'PAD_INVOICE', 994, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2024-09-27 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (491, 366, 'PAD_INVOICE', 994, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2024-09-27 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (492, 369, 'PAD_INVOICE', 972, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 18, 0, 'PAD 2024-10-04 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (493, 375, 'PAD_INVOICE', 972, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-10-04 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (494, 382, 'PAD_INVOICE', 950, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2024-10-11 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (495, 383, 'PAD_INVOICE', 950, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 17, 0, 'PAD 2024-10-11 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (496, 393, 'PAD_INVOICE', 950, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2024-10-11 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (497, 398, 'PAD_INVOICE', 931, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 18, 0, 'PAD 2024-10-18 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (498, 399, 'PAD_INVOICE', 931, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 18, 0, 'PAD 2024-10-18 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (499, 402, 'PAD_INVOICE', 931, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 15, 0, 'PAD 2024-10-18 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (500, 403, 'PAD_INVOICE', 931, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_4', 15, 0, 'PAD 2024-10-18 (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (501, 412, 'PAD_INVOICE', 900, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 16, 0, 'PAD 2024-10-25 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (502, 418, 'PAD_INVOICE', 900, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-10-25 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (503, 420, 'PAD_INVOICE', 877, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2024-11-01 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (504, 423, 'PAD_INVOICE', 877, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 16, 0, 'PAD 2024-11-01 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (505, 429, 'PAD_INVOICE', 877, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2024-11-01 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (506, 459, 'PAD_INVOICE', 831, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-11-15 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (507, 460, 'PAD_INVOICE', 831, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-11-15 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (508, 465, 'PAD_INVOICE', 810, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2024-11-22 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (509, 471, 'PAD_INVOICE', 797, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2024-11-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (510, 472, 'PAD_INVOICE', 797, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 18, 0, 'PAD 2024-11-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (511, 479, 'PAD_INVOICE', 797, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 15, 0, 'PAD 2024-11-29 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (512, 484, 'PAD_INVOICE', 759, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2024-12-06 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (513, 485, 'PAD_INVOICE', 759, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-12-06 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (514, 497, 'PAD_INVOICE', 738, NULL, NULL, 'HIGH', 'PAD_GFS_SUBSET_1', 15, 1, 'PAD 2024-12-13 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (515, 517, 'PAD_INVOICE', 711, NULL, NULL, 'HIGH', 'PAD_GFS_SUBSET_2', 15, 0, 'PAD 2024-12-20 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (516, 518, 'PAD_INVOICE', 711, NULL, NULL, 'HIGH', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-12-20 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (517, 521, 'PAD_INVOICE', 705, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 18, 0, 'PAD 2024-12-27 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (518, 529, 'PAD_INVOICE', 705, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2024-12-27 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (519, 540, 'PAD_INVOICE', 692, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-01-03 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (520, 546, 'PAD_INVOICE', 640, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 17, 0, 'PAD 2025-01-17 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (521, 548, 'PAD_INVOICE', 640, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2025-01-17 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (522, 562, 'PAD_INVOICE', 626, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2025-01-24 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (523, 563, 'PAD_INVOICE', 626, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2025-01-24 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (524, 572, 'PAD_INVOICE', 598, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 15, 0, 'PAD 2025-01-31 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (525, 573, 'PAD_INVOICE', 598, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2025-01-31 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (526, 574, 'PAD_INVOICE', 598, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_3', 14, 0, 'PAD 2025-01-31 (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (527, 584, 'PAD_INVOICE', 585, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2025-02-07 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (528, 585, 'PAD_INVOICE', 585, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_2', 14, 0, 'PAD 2025-02-07 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (529, 595, 'PAD_INVOICE', 552, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-02-14 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (530, 605, 'PAD_INVOICE', 543, NULL, NULL, 'HIGH', 'PAD_GFS_SUBSET_1', 15, 1, 'PAD 2025-02-21 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (531, 625, 'PAD_INVOICE', 497, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-03-07 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (532, 636, 'PAD_INVOICE', 481, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2025-03-14 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (533, 654, 'PAD_INVOICE', 424, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-03-28 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (534, 668, 'PAD_INVOICE', 412, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 15, 0, 'PAD 2025-04-04 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (535, 672, 'PAD_INVOICE', 392, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 18, 0, 'PAD 2025-04-11 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (536, 701, 'PAD_INVOICE', 341, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-05-30 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (537, 704, 'PAD_INVOICE', 323, NULL, NULL, 'EXACT', 'PAD_GFS_SUBSET_1', 14, 0, 'PAD 2025-06-13 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (538, 144, 'PAD_INVOICE', 1428, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 16, 0, 'PAD 2023-12-27 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (539, 176, 'PAD_INVOICE', 1322, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 16, 0, 'PAD 2024-02-07 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (540, 239, 'PAD_INVOICE', 1203, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 15, 0, 'PAD 2024-03-20 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (541, 258, 'PAD_INVOICE', 1187, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 14, 0, 'PAD 2024-03-27 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (542, 278, 'PAD_INVOICE', 1141, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 15, 0, 'PAD 2024-04-17 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (543, 312, 'PAD_INVOICE', 1100, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 14, 0, 'PAD 2024-05-22 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (544, 339, 'PAD_INVOICE', 1034, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 15, 0, 'PAD 2024-09-11 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (545, 392, 'PAD_INVOICE', 936, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 20, 0, 'PAD 2024-10-16 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (546, 424, 'PAD_INVOICE', 882, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 14, 0, 'PAD 2024-10-30 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (547, 463, 'PAD_INVOICE', 801, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_2', 20, 0, 'PAD 2024-11-27 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (548, 475, 'PAD_INVOICE', 801, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_2', 14, 0, 'PAD 2024-11-27 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (549, 539, 'PAD_INVOICE', 670, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 20, 0, 'PAD 2025-01-08 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (550, 560, 'PAD_INVOICE', 601, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_2', 20, 0, 'PAD 2025-01-29 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (551, 561, 'PAD_INVOICE', 601, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_2', 20, 0, 'PAD 2025-01-29 (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (552, 615, 'PAD_INVOICE', 500, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 20, 0, 'PAD 2025-03-05 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (553, 638, 'PAD_INVOICE', 427, NULL, NULL, 'EXACT', 'PAD_CAPITAL_SUBSET_1', 20, 0, 'PAD 2025-03-26 (1 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (554, 474, 'PAD_INVOICE', 724, NULL, NULL, 'HIGH', 'PAD_PEPSI_MONTHLY_1', 34, 528, 'Pepsi PAD 2024-12-16 [Auto-approved: exact amount match]');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (555, 622, 'PAD_INVOICE', 457, NULL, NULL, 'EXACT', 'PAD_PEPSI_MONTHLY_1', 25, 0, 'Pepsi PAD 2025-03-17');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (556, 661, 'PAD_INVOICE', 383, NULL, NULL, 'EXACT', 'PAD_PEPSI_MONTHLY_1', 29, 0, 'Pepsi PAD 2025-04-16');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (557, 334, 'CC_PAYMENT_TRANSFER', 1067, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 0, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (558, 346, 'CC_PAYMENT_TRANSFER', 985, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 29, 0, 'Amazon via CC payment to 8154');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (559, 435, 'CC_PAYMENT_TRANSFER', 865, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 13, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (560, 502, 'CC_PAYMENT_TRANSFER', 576, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 71, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (561, 648, 'CC_PAYMENT_TRANSFER', 459, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 6, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (562, 649, 'CC_PAYMENT_TRANSFER', 462, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 6, 1, 'Amazon via CC payment (1 cent diff)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (563, 650, 'CC_PAYMENT_TRANSFER', 461, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 6, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (564, 651, 'CC_PAYMENT_TRANSFER', 460, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 6, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (565, 686, 'CC_PAYMENT_TRANSFER', 371, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 9, 0, 'Amazon via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (566, 99, 'CC_PAYMENT_TRANSFER', 1564, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 2, 0, 'Costco via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (567, 172, 'CC_PAYMENT_TRANSFER', 1341, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 11, 0, 'Costco via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (568, 240, 'BILL_PAYMENT', 1253, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 1, 3, 'Costco via BMO MC bill pay');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (569, 482, 'CC_PAYMENT_TRANSFER', 822, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 0, 0, 'Costco via CC payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (570, 4, 'E_TRANSFER_REIMBURSE', 1618, NULL, NULL, 'HIGH', 'MANUAL_E_TRANSFER_REIMBURSE', 126, 0, 'Dwayne reimbursement for NS permit');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (571, 317, 'BILL_PAYMENT', 655, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 234, 0, 'Insurance bill payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (572, 49, 'CC_PAYMENT_TRANSFER', 1583, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 41, 0, 'Canadian Tire Gas via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (573, 50, 'CC_PAYMENT_TRANSFER', 1583, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 41, 0, 'Canadian Tire Gas via CC - DUPLICATE?');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (574, 75, 'CC_PAYMENT_TRANSFER', 1370, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 113, 0, 'Superstore via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (575, 81, 'CC_PAYMENT_TRANSFER', 1608, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 14, 0, 'Superstore via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (576, 101, 'CC_PAYMENT_TRANSFER', 1411, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 72, 0, 'Harrison Hardware via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (577, 303, 'CC_PAYMENT_TRANSFER', 1147, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', -8, 0, 'Superstore via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (578, 310, 'CC_PAYMENT_TRANSFER', 1117, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 0, 0, 'Superstore via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (579, 153, 'BILL_PAYMENT', 1230, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 67, 0, 'AliExpress via Neo MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (580, 155, 'BILL_PAYMENT', 1232, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 67, 0, 'AliExpress via Neo MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (581, 156, 'BILL_PAYMENT', 1231, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 67, 0, 'AliExpress via Neo MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (582, 277, 'E_TRANSFER_VENDOR', 1182, NULL, NULL, 'HIGH', 'MANUAL_E_TRANSFER_VENDOR', -1, 0, 'Markie B fan bus payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (583, 321, 'CHEQUE', 1090, NULL, NULL, 'HIGH', 'MANUAL_CHEQUE', 0, 0, 'Relay for Life donation');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (584, 523, 'BILL_PAYMENT', 772, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', -8, 0, 'Circle K via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (585, 537, 'BILL_PAYMENT', 574, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 55, 0, 'FloHockey via Triangle MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (586, 12, 'CC_PAYMENT_TRANSFER', 1557, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 117, 0, 'Pharmasave via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (587, 57, 'CC_PAYMENT_TRANSFER', 1584, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 36, 0, 'Pharmasave via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (588, 84, 'CC_PAYMENT_TRANSFER', 1601, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 11, 0, 'Pharmasave via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (589, 246, 'CC_PAYMENT_TRANSFER', 1116, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 60, 0, 'Pharmasave via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (590, 449, 'BILL_PAYMENT', 983, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', -27, 0, 'Pharmasave via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (592, 322, 'BILL_PAYMENT', 1081, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 5, 10, 'Sysco bill payment');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (593, 336, 'BILL_PAYMENT', 917, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 64, 1, 'Temu via Neo MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (594, 338, 'BILL_PAYMENT', 913, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 59, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (595, 364, 'BILL_PAYMENT', 912, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 40, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (596, 374, 'BILL_PAYMENT', 911, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 32, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (597, 433, 'BILL_PAYMENT', 914, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 0, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (598, 503, 'BILL_PAYMENT', 573, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 71, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (599, 504, 'BILL_PAYMENT', 572, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 71, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (600, 505, 'BILL_PAYMENT', 571, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', 71, 0, 'Temu via BMO MC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (601, 22, 'CC_PAYMENT_TRANSFER', 1538, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 84, 0, 'Walmart via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (602, 272, 'CC_PAYMENT_TRANSFER', 1236, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', -14, 0, 'Walmart via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (603, 35, 'CC_PAYMENT_TRANSFER', 1540, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 61, 0, 'Wholesale Club via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (604, 39, 'CC_PAYMENT_TRANSFER', 1577, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 50, 0, 'Wholesale Club via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (605, 628, 'CC_PAYMENT_TRANSFER', 516, NULL, NULL, 'HIGH', 'MANUAL_CC_PAYMENT_TRANSFER', 3, 0, 'Nayax via CC');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (606, 514, 'SPLIT_PAYMENT', 767, NULL, NULL, 'HIGH', 'MANUAL_SPLIT', 0, 0, 'Two e-transfers to Lil'' Em''s $46 each (bank_txn 767, 768)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (607, 64, 'E_TRANSFER_REIMBURSE', 1423, NULL, NULL, 'HIGH', 'MANUAL_REIMBURSE', 0, 0, 'Dwayne reimbursement');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (608, 154, 'BILL_PAYMENT', 1233, NULL, NULL, 'MEDIUM', 'MANUAL_APPROX', 0, 90, 'AliExpress - reimbursed wrong amount (short by $0.90)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (609, 323, 'SPLIT_PAYMENT', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', NULL, 0, 'June/May Rent $805 = 2x Thomas $402.50 on May 7');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (610, 191, 'SHAREHOLDER_REIMBURSE', 1382, NULL, NULL, 'HIGH', 'USER_MANUAL', 17, 0, 'Feb Rent $862.50 - Dwayne Jan 15 e-transfer (paid in advance)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (612, 455, 'SPLIT_PAYMENT', 762, NULL, NULL, 'HIGH', 'USER_MANUAL', 34, 0, 'Nov 2024 Rent $880 - Thomas Dec 5 e-transfer (combined with Dec)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (613, 501, 'SPLIT_PAYMENT', 762, NULL, NULL, 'HIGH', 'USER_MANUAL', 4, 0, 'Dec 2024 Rent $880 - Thomas Dec 5 e-transfer (combined with Nov)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 615, id, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'GFS damaged/pallet salvage - paid cash, no invoice' FROM wave_bills WHERE invoice_number = 'STUB-GFS-CASH-001' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 616, id, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'GFS damaged/pallet salvage - paid cash, no invoice' FROM wave_bills WHERE invoice_number = 'STUB-GFS-CASH-002' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 617, id, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'GFS damaged/pallet salvage - paid cash, no invoice' FROM wave_bills WHERE invoice_number = 'STUB-GFS-CASH-003' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 618, id, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'GFS damaged/pallet salvage - paid cash, no invoice' FROM wave_bills WHERE invoice_number = 'STUB-GFS-CASH-004' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (619, 166, 'INTERCOMPANY_PURCHASE', 1323, NULL, NULL, 'EXACT', 'EMAIL_NOTE_INVOICE', 24, 0, 'Email note match invoice Jan 14 oil damaged reimbursement. gfs 9005546522 (ref C1AWgjhaHcje)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (620, 25, 'INTERCOMPANY_PURCHASE', 1658, NULL, NULL, 'EXACT', 'EMAIL_NOTE_INVOICE', 38, 0, 'Email note match invoice GFS 9002908697 Aug 11 (ref C1AkVXdW3xAW)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (621, 126, 'SHAREHOLDER_REIMBURSE', 1390, NULL, NULL, 'HIGH', 'OLD_DB_NOTE_INVOICE', 0, 0, 'Old DB note invoice 9005534423: Reimbursement for: GFS - Bill 9005534423');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (622, 24, 'SHAREHOLDER_REIMBURSE', 1659, NULL, NULL, 'HIGH', 'OLD_DB_NOTE_INVOICE', 0, 0, 'Old DB note invoice 9002912093: Reimbursement for: GFS - Bill 9002912093');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (623, 7, 'SHAREHOLDER_REIMBURSE', 1660, NULL, NULL, 'HIGH', 'OLD_DB_NOTE_INVOICE', 0, 0, 'Old DB note invoice 9002186430: Reimbursement for: GFS - Bill 9002186430');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (624, 8, 'SHAREHOLDER_REIMBURSE', 1661, NULL, NULL, 'HIGH', 'OLD_DB_NOTE_INVOICE', 0, 0, 'Old DB note invoice 9002189920: Reimbursement for: GFS - Bill 9002189920');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (625, 5, 'SHAREHOLDER_REIMBURSE', 1662, NULL, NULL, 'HIGH', 'OLD_DB_NOTE_INVOICE', 0, 0, 'Old DB note invoice 9002081541: Reimbursement for: GFS - Bill 9002081541');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 626, id, 'SHAREHOLDER_REIMBURSE', 1503, NULL, NULL, 'HIGH', 'MANUAL_INVOICE_PDF', 0, 0, 'Invoice 1994069 inserted from PDF; missed in HST filings for FY2024' FROM wave_bills WHERE invoice_number = '1994069' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 627, id, 'VENDOR_ETRANSFER', 299, NULL, NULL, 'EXACT', 'MANUAL_INVOICE', 0, 0, 'Marketing: logo on ice sponsorship' FROM wave_bills WHERE invoice_number = 'RAMBLERS-LOGO-ICE-20250625' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 628, id, 'VENDOR_ETRANSFER', 300, NULL, NULL, 'EXACT', 'MANUAL_INVOICE', 0, 0, 'Marketing: golf tournament sponsorship' FROM wave_bills WHERE invoice_number = 'RAMBLERS-GOLF-20250625' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (629, 11, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'Paid via Dwayne personal CIBC (VISA debit); cash reimbursed off-bank.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (630, 42, 'SHAREHOLDER_REIMBURSE', 1641, NULL, NULL, 'HIGH', 'USER_MANUAL', 20, 0, 'Paid via Dwayne personal CIBC VISA debit 2023-09-15 (CAPITAL FOOD SE 325808175743); reimbursed via e-transfer 2023-09-27.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (631, 72, 'CASH_PAID', NULL, NULL, NULL, 'HIGH', 'USER_MANUAL', 0, 0, 'Statement invoice 2523999 = $1,064.63; +3% card fee. Paid via Dwayne personal card (Visa debit noted in chequing). Reimbursed to Dwayne in cash off-books (no bank txn).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (632, 86, 'CC_PURCHASE', NULL, 1505, 1540, 'HIGH', 'USER_MANUAL', 19, 0, 'Statement invoice 2526446 = $1,010.54; +3% card fee. Charged to CIBC Visa 0318 on 2023-10-31; linked to Visa payment 2023-11-01.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (633, 131, 'CC_PURCHASE', NULL, 1458, 1489, 'HIGH', 'USER_MANUAL', -6, 0, 'Statement invoice 2530298 = $929.00; +3% card fee. Charged to CIBC Visa 0318 on 2023-11-14; linked to Visa payment 2023-11-27.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (635, 674, 'SPLIT_PAYMENT', NULL, 387, NULL, 'HIGH', 'MANUAL_SPLIT', 42, 0, 'Bell catch-up payment $408.58 covers Mar/Apr + late fees; Feb paid via direct bank bill payment (carry-forward credit applied to post-FY bills) FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (636, 691, 'SPLIT_PAYMENT', NULL, 387, NULL, 'HIGH', 'MANUAL_SPLIT', 12, 0, 'Bell catch-up payment $408.58 covers Mar/Apr + late fees; Feb paid via direct bank bill payment (carry-forward credit applied to post-FY bills) FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (637, 695, 'SPLIT_PAYMENT', NULL, 387, NULL, 'HIGH', 'MANUAL_SPLIT', 12, 0, 'Bell catch-up payment $408.58 covers Mar/Apr + late fees; Feb paid via direct bank bill payment (carry-forward credit applied to post-FY bills) FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (639, 705, 'CC_PURCHASE', NULL, 348, NULL, 'HIGH', 'BELL_AUTOPAY', 12, 0, 'Bell monthly autopay (Canteen account) FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (640, 627, 'BANK_DEBIT', 569, NULL, NULL, 'HIGH', 'MANUAL_BILL_PAYMENT', -17, 0, 'Direct bank bill payment (Canteen) - manual match FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (641, 365, 'SPLIT_PAYMENT', NULL, NULL, NULL, 'HIGH', 'MANUAL_CC_SPLIT', 1, 0, 'Split across CC txns 3495/3496/3497 (DOLLARAMA # 209) on 2024-09-13: $100.00 + $100.00 + $121.65 (CIBC Mastercard 8154).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (642, 547, 'BANK_DEBIT', 490, NULL, NULL, 'HIGH', 'MANUAL_RENT_DEBIT', 68, 0, 'Town of Amherst rent - matched to debit card payment bank_txn 490.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (643, 679, 'BANK_DEBIT', 463, NULL, NULL, 'HIGH', 'MANUAL_RENT_DEBIT', -15, 0, 'Town of Amherst rent - matched to debit card payment bank_txn 463.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (644, 610, 'PAD_INVOICE', 588, NULL, NULL, 'HIGH', 'MANUAL_PAD_MATCH', -7, 0, 'Manual PAD match to Capital Foods bank_txn 588.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (645, 599, 'PAD_INVOICE', 400, NULL, NULL, 'HIGH', 'MANUAL_PAD_MATCH', 65, 0, 'Manual PAD match to Capital Foods bank_txn 400.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (646, 220, 'PAD_INVOICE', 1242, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_4', 18, 0, 'EFT Notification_10.XLS (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (647, 216, 'PAD_INVOICE', 1242, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_4', 19, 0, 'EFT Notification_10.XLS (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (648, 222, 'PAD_INVOICE', 1242, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_4', 15, 0, 'EFT Notification_10.XLS (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (649, 224, 'PAD_INVOICE', 1242, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_4', 14, 0, 'EFT Notification_10.XLS (4 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (650, 182, 'PAD_INVOICE', 1320, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_3', 15, 0, 'EFT Notification_14.XLS (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (651, 274, 'PAD_INVOICE', 1154, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_2', 15, 0, 'EFT Notification_5.XLS (2 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (652, 266, 'PAD_INVOICE', 1171, NULL, NULL, 'EXACT', 'PAD_GFS_EFT_FILE_3', 16, 0, 'EFT Notification_7.XLS (3 invoices)');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (656, 2, 'CASH_PAID', NULL, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'Paid in cash off-bank (Mondoux).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (657, 18, 'SPLIT_PAYMENT', 1683, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'CIBC monthly fees aggregated from bank_txn_ids: 1688, 1683, 1684, 1685');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (658, 31, 'SPLIT_PAYMENT', 1676, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'CIBC monthly fees aggregated from bank_txn_ids: 1676, 1677');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (659, 1, 'SHAREHOLDER_REIMBURSE', 1639, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'Sept 27 e-transfer to Dwayne: June full rent $700 + HST = $805.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (660, 13, 'SHAREHOLDER_REIMBURSE', 1689, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'July rent paid by Dwayne, reimbursed via Jul 5 transfer to 00153/19-23218 ($402.50).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (661, 19, 'BANK_DEBIT', 1681, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'August rent paid direct via debit card to Town of Amherst ($402.50).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (662, 78, 'CC_PAYMENT_TRANSFER', 1529, NULL, NULL, NULL, 'MANUAL_CC_PAYMENT_TRANSFER', 30, 37, 'Amazon via CC payment transfer 000000206582 (amount diff $0.37).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (663, 82, 'CC_PAYMENT_TRANSFER', 1570, NULL, NULL, NULL, 'MANUAL_CC_PAYMENT_TRANSFER', 14, -544, 'Atlantic Superstore via CC payment transfer 000000103415 (amount diff $5.44).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (664, 94, 'CC_PAYMENT_TRANSFER', 1596, NULL, NULL, NULL, 'MANUAL_CC_PAYMENT_TRANSFER', 6, 0, 'Amazon corrected to $167.85; repaid to Mastercard Oct 21 (bank transfer 000000122519).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (665, 95, 'CASH_PAID', NULL, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'Paid by Tom; reimbursed in cash off-bank.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (666, 106, 'CC_PAYMENT_TRANSFER', 1539, NULL, NULL, NULL, 'MANUAL_CC_PAYMENT_TRANSFER', 7, 0, 'Black Cat paid by Mastercard (Nova 1); repaid via bank transfer 000000221703.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (667, 125, 'CASH_PAID', NULL, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'Paid in cash; reimbursed in cash off-bank.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (668, 148, 'SPLIT_PAYMENT', 1405, NULL, NULL, NULL, 'USER_MANUAL', 17, 0, 'GFS EFT batch 67876-000003063: invoice 9005510560 netted with credit memo 9005357713-CR; bank credit $204.51 on 2024-01-05.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 669, id, 'SPLIT_PAYMENT', 1405, NULL, NULL, NULL, 'USER_MANUAL', 18, 0, 'GFS credit memo 9005357713-CR in EFT batch 67876-000003063; net bank credit $204.51 on 2024-01-05.' FROM wave_bills WHERE invoice_number = '9005357713-CR' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (670, 151, 'CC_PAYMENT_TRANSFER', 1124, NULL, NULL, NULL, 'MANUAL_CC_PAYMENT_TRANSFER', 121, 0, 'Shopify order screen (4x $22.99 USD Sep-Dec 2023) paid via Visa; reimbursed by CC payment Apr 30, 2024.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (671, 152, 'SPLIT_PAYMENT', 1543, NULL, NULL, NULL, 'USER_MANUAL', -61, 0, 'CIBC account fees aggregated for Oct-Dec 2023: bank_txn_ids 1543, 1481, 1419.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 672, id, 'SPLIT_PAYMENT', 1629, NULL, NULL, NULL, 'USER_MANUAL', -1, 0, 'CIBC account fees for Sep 2023: bank_txn_ids 1629, 1632, 1633, 1630, 1631.' FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (673, 185, 'CASH_PAID', NULL, NULL, NULL, NULL, 'USER_MANUAL', NULL, 0, 'Paid from till (cash off-bank).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 674, id, 'BILL_PAYMENT', 1461, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 0, 0, 'Triangle fuel receipt placeholder (no card statement).' FROM wave_bills WHERE invoice_number = 'FUEL-TRIANGLE-20231206' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 675, id, 'BILL_PAYMENT', 1425, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 0, 0, 'Triangle fuel receipt placeholder (no card statement).' FROM wave_bills WHERE invoice_number = 'FUEL-TRIANGLE-20231228' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (676, 230, 'BILL_PAYMENT', 1229, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 14, 304, 'AliExpress bill paid via Neo Mastercard bill payment; amount off by $3.04.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (677, 209, 'BILL_PAYMENT', 1291, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 7, 0, 'Cafe Archibald paid via Triangle Mastercard bill payment.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 678, id, 'BILL_PAYMENT', 1248, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 0, 0, 'Costco receipt placeholder (BMO Mastercard payment).' FROM wave_bills WHERE invoice_number = 'COSTCO-RECEIPT-20240306' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (679, 281, 'BILL_PAYMENT', 1173, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 1, 0, 'Circle K fuel paid via BMO Mastercard bill payment.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (680, 284, 'BILL_PAYMENT', 1166, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 4, 0, 'Pharmasave bill paid via BMO Mastercard bill payment.');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (681, 296, 'BILL_PAYMENT', 1149, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 2, 24, 'Shell gas paid via BMO Mastercard bill payment (amount diff $0.24).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (682, 612, 'BILL_PAYMENT', 575, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', -2, -383, 'Esso bill paid via NEO Mastercard bill payment. (amount diff $-3.83).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (683, 452, 'BILL_PAYMENT', 859, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 7, -40, 'Christmas Discounters bill paid via BMO Mastercard bill payment. (amount diff $-0.40).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (684, 631, 'BILL_PAYMENT', 518, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 2, -637, 'Circle K bill paid via BMO Mastercard bill payment. (amount diff $-6.37).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (685, 371, 'BILL_PAYMENT', 977, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 15, 2755, 'Walmart bill paid via NEO Mastercard bill payment (amount diff $27.55).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (686, 425, 'BILL_PAYMENT', 856, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 21, 0, 'Costco bill paid via BMO Mastercard bill payment (Oct 16 purchase).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 687, id, 'E_TRANSFER_REIMBURSE', 845, NULL, NULL, NULL, 'MANUAL_E_TRANSFER_REIMBURSE', 1, 0, 'Thomas reimbursement for Pharmasave (Nov 11, 2024 bill).' FROM wave_bills WHERE invoice_number = 'PHARMASAVE-RECEIPT-20241111' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (688, 645, 'BILL_PAYMENT', 432, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 18, -820, 'Value Village bill paid via NEO Mastercard bill payment. (amount diff $-8.20).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (689, 385, 'BILL_PAYMENT', 857, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 42, 633, 'Circle K bill paid via Triangle Mastercard bill payment. (amount diff $6.33).');
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 690, id, 'BILL_PAYMENT', 843, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 0, 0, 'Fuel receipt placeholder (BMO Mastercard payment).' FROM wave_bills WHERE invoice_number = 'FUEL-RECEIPT-20241112' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 691, id, 'BILL_PAYMENT', 521, NULL, NULL, NULL, 'MANUAL_BILL_PAYMENT', 0, 0, 'Fuel receipt placeholder (BMO Mastercard payment).' FROM wave_bills WHERE invoice_number = 'FUEL-RECEIPT-20250227' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 692, id, 'SPLIT_PAYMENT', 1690, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'CIBC June 2023 fees aggregated: bank_txn_ids 1690, 1691, 1692, 1693.' FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-06' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 693, id, 'BANK_DEBIT', 1679, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'DEBIT_CARD (manual receipt placeholder).' FROM wave_bills WHERE invoice_number = 'STUB-WALMART-COGS-20230814' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 694, id, 'BANK_DEBIT', 1680, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'DEBIT_CARD (manual receipt placeholder).' FROM wave_bills WHERE invoice_number = 'STUB-DOLLARAMA-COGS-20230814' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 695, id, 'SHAREHOLDER_REIMBURSE', 1617, NULL, NULL, NULL, 'USER_MANUAL', 0, 0, 'Thomas reimbursement for GFS cash off-books bill (no invoice).' FROM wave_bills WHERE invoice_number = 'STUB-GFS-CASH-COGS-20231011' LIMIT 1;
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) SELECT 696, id, 'SHAREHOLDER_REIMBURSE', 1640, NULL, NULL, NULL, 'USER_MANUAL', 22, 0, 'Dwayne reimbursement for Walmart purchase (original bill missing; placeholder).' FROM wave_bills WHERE invoice_number = 'STUB-WALMART-REIMBURSE-20230905' LIMIT 1;
DELETE FROM split_payments;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (1, 323, 'BANK', 1113, 40250);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (2, 323, 'BANK', 1114, 40250);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (3, 455, 'BANK', 762, 88000);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (4, 501, 'BANK', 762, 88000);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (5, 514, 'BANK', 767, 4600);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (6, 514, 'BANK', 768, 4600);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (7, 365, 'CC', 3495, 10000);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (8, 365, 'CC', 3496, 10000);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (9, 365, 'CC', 3497, 12165);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (13, 18, 'BANK', 1688, 500);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (14, 18, 'BANK', 1683, 600);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (15, 18, 'BANK', 1684, 125);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (16, 18, 'BANK', 1685, 200);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (17, 31, 'BANK', 1676, 600);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (18, 31, 'BANK', 1677, 500);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (19, 148, 'BANK', 1405, 47583);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 20, id, 'BANK', 1405, -68034 FROM wave_bills WHERE invoice_number = '9005357713-CR' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (21, 152, 'BANK', 1543, 6500);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (22, 152, 'BANK', 1481, 6500);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) VALUES (23, 152, 'BANK', 1419, 6500);
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 24, id, 'BANK', 1629, 600 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 25, id, 'BANK', 1632, 250 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 26, id, 'BANK', 1633, 4000 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 27, id, 'BANK', 1690, 600 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-06' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 28, id, 'BANK', 1691, 22 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-06' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 29, id, 'BANK', 1692, 200 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-06' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 30, id, 'BANK', 1693, 125 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-06' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 31, id, 'BANK', 1630, 1950 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
INSERT INTO split_payments (id, wave_bill_id, txn_type, txn_id, amount_cents) SELECT 32, id, 'BANK', 1631, 1125 FROM wave_bills WHERE invoice_number = 'CIBC-FEES-2023-09' LIMIT 1;
DELETE FROM bank_txn_classifications;
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (1, 377, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne - $20,000', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (2, 688, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne - $5,000', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (3, 1085, 'THOMAS', 'PAYROLL', 'Payroll to Thomas - $4,321.07', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (4, 1086, 'DWAYNE', 'LOAN_ISSUED', 'Shareholder loan to Dwayne - $9,000', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (5, 1090, 'CORP', 'DONATION', 'Donation to Relay for Life (Canadian Cancer Society) - $110.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (6, 1645, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 70)', '70', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (7, 1542, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 110)', '110', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (8, 1478, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 111)', '111', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (9, 1447, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 145)', '145', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (10, 1148, 'THOMAS', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 276)', '276', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (11, 1074, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 328)', '328', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (12, 782, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 495)', '495', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (13, 683, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 525)', '525', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (14, 1669, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $127.50', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (15, 1658, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $123.91 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (16, 1659, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1157.64 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (17, 1660, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $140.04 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (18, 1661, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $102.50 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (19, 1662, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $265.68 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (20, 1663, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $222.21', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (21, 1647, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $118.37', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (22, 1639, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $805.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (23, 1640, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Walmart - Bill (Sep 5, 2023 placeholder)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (24, 1641, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 42)', '42', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (25, 1630, 'CORP', 'BANK_FEE', 'CIBC per-transfer fee (account not unlimited at the time)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (26, 1627, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $263.60', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (27, 1622, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $266.46', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (28, 1617, 'THOMAS', 'REIMBURSEMENT', 'Thomas reimbursement for: GFS - Bill (cash off books)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (29, 1618, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $222.59 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (30, 1615, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $862.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (31, 1612, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $170.36', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (32, 1566, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $266.46', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (33, 1568, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $200.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (34, 1569, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $95.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (35, 1572, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $104.10 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (36, 1576, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $538.75 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (37, 1546, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $310.03', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (38, 1536, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $88.80 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (39, 1524, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $352.29', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (40, 1525, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $95.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (41, 1526, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $265.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (42, 1508, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $85.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (43, 1509, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $271.40', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (44, 1510, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Maddison Troop - $59.02', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (45, 1511, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $264.97', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (46, 1503, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 1994069 (PDF; missed HST FY2024)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (47, 1504, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1437.22 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (48, 1498, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $170.36', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (49, 1487, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Maddison Troop - $77.47', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (50, 1488, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $211.95', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (51, 1485, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $372.67', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (52, 1477, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $116.87 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (53, 1465, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $159.96', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (54, 1448, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $72.25', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (55, 1449, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $194.62', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (56, 1450, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $36.50 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (57, 1451, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $148.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (58, 1452, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $100.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (59, 1444, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $473.50', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (60, 1446, 'UNKNOWN', 'DONATION', 'Sponsorship of kid''s hockey team/jersey (Tim Rich)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (61, 1438, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $146.10', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (62, 1430, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $495.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (63, 1431, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $2000.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (64, 1423, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $9.88 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (65, 1418, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $177.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (66, 1408, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $213.90 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (67, 1390, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $2000.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (68, 1382, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $862.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (69, 1380, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $592.18', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (70, 1364, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $101.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (71, 1365, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1541.41 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (72, 1366, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $41.01', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (73, 1367, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $91.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (74, 1362, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $114.82', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (75, 1350, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $40.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (76, 1352, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $621.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (77, 1353, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $279.05', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (78, 1329, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $169.75', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (79, 1323, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $400.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (80, 1314, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $726.68', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (81, 1315, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $240.85', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (82, 1307, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $285.98', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (83, 1285, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $20.69 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (84, 1276, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-01', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (85, 1277, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $72.02 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (86, 1278, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $893.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (87, 1279, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $246.11', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (88, 1280, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (89, 1266, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $17.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (90, 1258, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $200.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (91, 1260, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $111.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (92, 1255, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $566.16 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (93, 1228, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1305.38', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (94, 1237, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $558.47 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (95, 1238, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.82', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (96, 1239, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $223.32', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (97, 1240, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $168.79', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (98, 1212, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $169.75', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (99, 1213, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $189.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (100, 1196, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $79.04', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (101, 1197, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1277.17', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (102, 1198, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $263.63', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (103, 1199, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $151.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (104, 1182, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT MARKIE B'' - $1311.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (105, 1178, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (106, 1179, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $49.09', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (107, 1163, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1065.27', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (108, 1164, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (109, 1165, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $119.31', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (110, 1152, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $257.05', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (111, 1153, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $233.39', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (112, 1132, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $844.09', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (113, 1133, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $178.23', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (114, 1134, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $297.54', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (115, 1128, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT CHARLIE'' - $30.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (116, 1122, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-04', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (117, 1113, 'THOMAS', 'RENT_REIMBURSEMENT', 'Rent reimbursement to THOMAS - $402.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (118, 1114, 'THOMAS', 'RENT_REIMBURSEMENT', 'Rent reimbursement to THOMAS - $402.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (119, 1110, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $70.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (120, 1080, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $125.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (121, 1077, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $402.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (122, 1071, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $18.56 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (123, 1063, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $105.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (124, 1064, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $95.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (125, 1051, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (126, 1060, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $81.83', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (127, 1061, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (128, 1042, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1282.50 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (129, 1043, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $68.86', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (130, 1044, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $265.82', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (131, 1045, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $307.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (132, 1036, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $412.29', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (133, 1026, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $134.68', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (134, 1027, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $201.46', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (135, 1028, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $77.51', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (136, 1029, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $78.84', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (137, 1003, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (138, 1004, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $409.97', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (139, 1005, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $198.09', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (140, 1006, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $142.85', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (141, 1007, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $64.43', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (142, 997, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $200.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (143, 998, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $100.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (144, 988, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $90.49', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (145, 989, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $318.40', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (146, 990, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (147, 991, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $259.25', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (148, 959, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $737.76', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (149, 960, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (150, 961, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $363.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (151, 962, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $178.40', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (152, 963, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $63.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (153, 965, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-09', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (154, 946, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $142.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (155, 947, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $116.42', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (156, 948, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $253.99', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (157, 949, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $202.83', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (158, 925, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $899.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (159, 926, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (160, 927, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $174.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (161, 928, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $421.48', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (162, 929, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $187.05', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (163, 909, 'THOMAS', 'HST_REIMBURSEMENT', 'HST reimbursement to THOMAS Q1 2025', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (164, 895, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $329.65', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (165, 896, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $349.43', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (166, 897, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $125.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (167, 898, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $191.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (168, 867, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $389.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (169, 868, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $886.31', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (170, 869, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $268.46', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (171, 870, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $240.85', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (172, 840, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $367.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (173, 845, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $31.44 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (174, 849, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $81.83', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (175, 850, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $212.51', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (176, 851, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $279.84', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (177, 817, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $93.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (178, 818, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $421.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (179, 826, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $176.96', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (180, 827, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $176.96', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (181, 828, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $258.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (182, 830, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $402.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (183, 814, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $779.21', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (184, 807, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $240.41', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (185, 808, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $181.77', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (186, 809, 'VENDOR', 'UNINVOICED_PAYMENT', 'Payment for stickers (uninvoiced) - $20.69', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (187, 802, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $63.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (188, 803, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $142.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (189, 791, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $909.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (190, 792, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $449.69', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (191, 793, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $274.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (192, 794, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $450.67', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (193, 777, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $254.74 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (194, 767, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to LIL'' EM''S - $46.00 (split for Wave bill 514)', '514', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (195, 768, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to LIL'' EM''S - $46.00 (split for Wave bill 514)', '514', 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (196, 770, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $50.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (197, 762, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1760.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (198, 748, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $279.84', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (199, 749, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $133.72', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (200, 750, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $282.48', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (201, 751, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $29.25', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (202, 752, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $226.38', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (203, 757, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $496.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (204, 731, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $642.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (205, 732, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $238.53', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (206, 733, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $380.85', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (207, 734, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $428.64', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (208, 735, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $309.90', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (209, 737, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT U9 DEV D'' - $200.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (210, 715, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $12.21 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (211, 716, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $400.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (212, 717, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $230.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (213, 718, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1500.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (214, 708, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $182.72', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (215, 709, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $142.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (216, 702, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (217, 703, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (218, 697, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1500.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (219, 690, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $249.23', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (220, 691, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $196.22', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (221, 671, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $93.90', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (222, 672, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $50.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (223, 673, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $61.44', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (224, 674, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $230.95', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (225, 675, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $534.30', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (226, 676, 'THOMAS', 'OWNER_DRAW', 'Owner draw to Thomas - $1,000', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (227, 660, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $173.15', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (228, 661, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $242.35', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (229, 662, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $276.14', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (230, 663, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $366.92', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (231, 664, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $431.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (232, 641, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $500.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (233, 632, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $75.52', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (234, 633, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $75.52', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (235, 634, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $228.81', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (236, 635, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $201.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (237, 636, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $348.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (238, 637, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.25', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (239, 639, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $218.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (240, 611, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $166.01 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (241, 619, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $72.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (242, 620, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $72.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (243, 621, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $169.56', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (244, 622, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $319.65', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (245, 623, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $402.44', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (246, 624, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $370.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (247, 592, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $51.97', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (248, 593, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $56.30', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (249, 594, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $251.98', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (250, 595, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $328.14', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (251, 579, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $69.01', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (252, 580, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $170.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (253, 581, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $224.56', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (254, 582, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $375.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (255, 583, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $430.22', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (256, 546, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $277.27', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (257, 547, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $245.62', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (258, 548, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $357.30', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (259, 549, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $472.74', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (260, 535, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $87.80', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (261, 536, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $149.88', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (262, 537, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $144.65', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (263, 538, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $299.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (264, 539, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $290.18', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (265, 527, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $73.64 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (266, 506, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $79.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (267, 507, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $188.44', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (268, 508, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $201.01', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (269, 509, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $348.55', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (270, 489, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $181.69', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (271, 491, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $208.40', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (272, 492, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $99.44', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (273, 493, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $208.40', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (274, 494, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $342.24', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (275, 495, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $385.75', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (276, 482, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (277, 483, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $500.00 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (278, 476, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $81.38', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (279, 477, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $147.99', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (280, 478, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $299.05', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (281, 479, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $336.98', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (282, 435, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $172.41', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (283, 436, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $103.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (284, 437, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $219.04', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (285, 438, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $296.37', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (286, 419, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $73.25', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (287, 420, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $138.30', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (288, 421, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $152.99', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (289, 422, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $225.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (290, 408, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $118.54', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (291, 409, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $302.21', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (292, 410, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $180.86', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (293, 388, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $96.26', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (294, 389, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $319.15', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (295, 390, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $310.10', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (296, 384, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (297, 378, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (298, 379, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $219.74', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (299, 380, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $249.14', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (300, 364, 'THOMAS', 'OWNER_DRAW', 'Owner draw to Thomas - $2,900', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (301, 365, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $80.89', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (302, 362, 'THOMAS', 'LOAN_ISSUED', 'Shareholder loan to Thomas - $2,000', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (303, 363, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $610.15 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (304, 358, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $111.64', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (305, 351, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (306, 349, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (307, 329, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT AUCTIONS'' - $783.75', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (308, 327, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (309, 328, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $100.35', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (310, 324, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT TERRI'' - $100.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (311, 314, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (312, 304, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (313, 305, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $64.63', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (314, 299, 'VENDOR', 'VENDOR_ETRANSFER', 'Amherst Ramblers - Marketing: logo on ice sponsorship - $1250.00', CAST((SELECT id FROM wave_bills WHERE invoice_number = 'RAMBLERS-LOGO-ICE-20250625' LIMIT 1) AS TEXT), 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (315, 300, 'VENDOR', 'VENDOR_ETRANSFER', 'Amherst Ramblers - Marketing: golf tournament sponsorship - $150.00', CAST((SELECT id FROM wave_bills WHERE invoice_number = 'RAMBLERS-GOLF-20250625' LIMIT 1) AS TEXT), 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (316, 296, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (317, 293, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (318, 294, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $50.64', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (319, 290, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (320, 288, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $34.02 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (321, 287, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (322, 284, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $134.71', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (323, 281, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $192.38', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (324, 275, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $203.90', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (325, 276, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (326, 274, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (327, 258, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $219.28', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (328, 259, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $88.58', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (329, 260, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $274.64', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (330, 255, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT DEAN TUP'' - $100.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (331, 248, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $104.55', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (332, 249, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $88.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (333, 250, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $218.18', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (334, 251, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $435.36', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (335, 252, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $614.17', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (336, 234, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $194.66', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (337, 235, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $134.08', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (338, 236, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $172.09', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (339, 224, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $60.67', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (340, 225, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $128.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (341, 226, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $342.11', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (342, 227, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $494.27', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (343, 209, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $175.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (344, 210, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $77.14', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (345, 211, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $227.61', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (346, 212, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $306.31', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (347, 213, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $448.11', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (348, 189, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $283.46', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (349, 190, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $132.59', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (350, 191, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $275.29', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (351, 192, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $405.19', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (352, 175, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT MATT SEL'' - $300.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (353, 176, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $154.70', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (354, 177, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $388.23', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (355, 178, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $213.10', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (356, 179, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $289.17', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (357, 180, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.81', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (358, 169, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to COVERED BRIDGE - $933.43 (needs Wave bill)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (359, 158, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $312.58', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (360, 159, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $490.65', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (361, 160, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $540.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (362, 161, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $571.76', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (363, 162, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $637.51', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (364, 130, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT AMHERST'' - $142.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (365, 113, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $192.26', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (366, 114, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $509.10', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (367, 115, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $335.82', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (368, 116, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $407.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (369, 117, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $552.45', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (370, 100, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $142.05', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (371, 101, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $455.97', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (372, 102, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $229.48', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (373, 103, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $470.07', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (374, 104, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $493.88', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (375, 87, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to COVERED BRIDGE - $364.07 (needs Wave bill)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (376, 74, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $70.46', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (377, 75, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $364.73', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (378, 76, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $110.87', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (379, 77, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $333.34', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (380, 78, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $366.25', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (381, 80, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT'' - $132.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (382, 52, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $339.16', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (383, 53, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $168.71', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (384, 54, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $394.90', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (385, 55, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $238.02', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (386, 56, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $424.46', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (387, 57, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $492.35', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (388, 39, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Amanda Willet - $161.74', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (389, 40, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $423.42', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (390, 41, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $295.64', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (391, 42, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $363.61', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (392, 43, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $375.55', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (393, 12, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Amanda Willet - $74.47', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (394, 13, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $345.77', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (395, 14, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $199.98', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (396, 15, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $305.74', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (397, 16, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $332.12', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (398, 5, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $914.18 (needs invoice)', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (399, 3, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT JAMIE MA'' - $415.30', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (400, 10, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (401, 27, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2025-10', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (402, 28, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2025-09', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (403, 257, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (404, 279, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $42.57', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (405, 295, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (406, 298, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2999.56', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (407, 330, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $257.17', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (408, 338, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (409, 352, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $929.60', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (410, 360, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (411, 375, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $8231.53', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (412, 387, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $1240.32', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (413, 416, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $6.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (414, 458, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $27.29', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (415, 503, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $589.74', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (416, 504, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $772.79', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (417, 505, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (418, 568, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $796.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (419, 591, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (420, 657, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2572.87', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (421, 689, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (422, 761, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2289.89', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (423, 789, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $8.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (424, 798, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2542.18', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (425, 834, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $3064.77', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (426, 835, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $3774.16', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (427, 862, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2024-10', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (428, 346, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne (transfer)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (429, 540, 'CORP', 'INTERNAL_TRANSFER', 'Internal transfer - $5070.00', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (430, 1689, 'CORP', 'INTERNAL_TRANSFER', 'Internal transfer - $402.50', NULL, 0);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (431, 19, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (432, 105, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (433, 208, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (434, 269, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (435, 282, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (436, 297, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (437, 340, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (438, 345, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (439, 361, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (440, 418, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (441, 511, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (442, 533, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (443, 596, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (444, 696, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (445, 796, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (446, 879, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (447, 993, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (448, 1062, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (449, 1076, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (450, 1082, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (451, 1092, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (452, 1123, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (453, 1184, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (454, 1264, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (455, 1339, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (456, 1419, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (457, 1481, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (458, 1543, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (459, 1629, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (460, 1632, 'CORP', 'BANK_FEE', 'Bank service fee - $2.50', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (461, 1633, 'CORP', 'BANK_FEE', 'Bank service fee - $40.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (462, 1676, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (463, 1677, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (464, 1683, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (465, 1684, 'CORP', 'BANK_FEE', 'Bank service fee - $1.25', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (466, 1685, 'CORP', 'BANK_FEE', 'Bank service fee - $2.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (467, 1688, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (468, 1690, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (469, 1692, 'CORP', 'BANK_FEE', 'Bank service fee - $2.00', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (470, 1693, 'CORP', 'BANK_FEE', 'Bank service fee - $1.25', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (471, 383, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (472, 457, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (473, 487, 'CORP', 'VENDOR_PAYMENT', 'Sysco vendor payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (474, 512, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (475, 515, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (476, 551, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (477, 569, 'CORP', 'UTILITIES', 'Bell Aliant phone/internet', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (478, 597, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (479, 643, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (480, 655, 'CORP', 'INSURANCE', 'BFL Insurance payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (481, 684, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (482, 724, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (483, 781, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Walmart - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (484, 785, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Dollarama - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (485, 787, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (486, 790, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: GFS - Bill 9013824877', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (487, 816, 'CORP', 'EFT_PAYMENT', 'EFT misc payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (488, 880, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (489, 884, 'UNKNOWN', 'CASH_WITHDRAWAL', 'ATM/branch cash withdrawal', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (490, 894, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (491, 903, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (492, 935, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (493, 937, 'UNKNOWN', 'CASH_WITHDRAWAL', 'ATM/branch cash withdrawal', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (494, 953, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Shell Gas - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (495, 954, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 3110269', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (496, 1052, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Facebook Marketplace - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (497, 1057, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Atlantic Superstore - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (498, 1059, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 30000969', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (499, 1081, 'CORP', 'VENDOR_PAYMENT', 'Sysco vendor payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (500, 1106, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (501, 1109, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Bridge Workshop - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (502, 1131, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 25', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (503, 1143, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (504, 1151, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (505, 1185, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (506, 1211, 'CORP', 'EFT_PAYMENT', 'EFT misc payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (507, 1223, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2425069', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (508, 1224, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2437469', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (509, 1225, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Town of Amherst - Bill March Rent', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (510, 1243, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2423469', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (511, 1284, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2365969', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (512, 1286, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Jeff Bembridge - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (513, 1287, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Electric Kitty - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (514, 1324, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: GFS - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (515, 1351, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Town of Amherst - Bill FEbruary REnt', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (516, 1363, 'CORP', 'INSURANCE', 'BFL Insurance payment', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (517, 1396, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2220169', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (518, 1492, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Town of Amherst - Bill', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (519, 1521, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill D1', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (520, 1559, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Mondoux - Bill 8100383', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (521, 1631, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (522, 1656, 'VENDOR', 'VENDOR_PAYMENT', 'Covered Bridge Chips vendor', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (523, 1691, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (524, 347, 'DWAYNE', 'LOAN_REPAID', 'Loan repaid by Dwayne (transfer)', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (525, 309, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (526, 312, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (527, 315, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (528, 316, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (529, 333, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (530, 367, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (531, 370, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (532, 403, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (533, 405, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (534, 432, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (535, 445, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (536, 465, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (537, 467, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (538, 473, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (539, 474, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (540, 518, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (541, 521, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (542, 522, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (543, 561, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (544, 563, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (545, 566, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (546, 571, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (547, 572, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (548, 573, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (549, 574, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (550, 575, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (551, 604, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (552, 607, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (553, 651, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (554, 668, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (555, 682, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (556, 700, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (557, 712, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (558, 725, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (559, 727, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (560, 728, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (561, 730, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (562, 742, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (563, 743, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (564, 755, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (565, 772, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (566, 776, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (567, 819, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (568, 820, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (569, 843, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (570, 847, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (571, 848, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (572, 856, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (573, 857, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (574, 859, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (575, 860, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (576, 864, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (577, 875, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (578, 876, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (579, 888, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (580, 890, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (581, 893, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (582, 904, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (583, 905, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (584, 910, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (585, 911, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (586, 912, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (587, 913, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (588, 914, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (589, 915, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (590, 916, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (591, 917, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (592, 922, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (593, 923, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (594, 942, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (595, 943, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (596, 944, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (597, 969, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (598, 970, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (599, 976, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (600, 977, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (601, 981, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (602, 983, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (603, 984, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (604, 1008, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (605, 1012, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (606, 1013, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (607, 1014, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (608, 1015, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (609, 1019, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (610, 1038, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (611, 1041, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (612, 1048, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (613, 1055, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (614, 1058, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (615, 1069, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (616, 1149, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (617, 1166, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (618, 1173, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (619, 1189, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (620, 1190, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (621, 1218, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (622, 1229, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (623, 1230, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (624, 1231, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (625, 1232, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (626, 1233, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (627, 1234, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (628, 1247, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (629, 1248, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (630, 1251, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (631, 1253, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (632, 1273, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (633, 1290, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (634, 1291, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (635, 1294, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (636, 1296, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (637, 1297, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (638, 1301, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (BMO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (639, 1316, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (NEO) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (640, 1317, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (641, 1425, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (642, 1461, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
INSERT INTO bank_txn_classifications (id, bank_txn_id, entity, txn_category, explanation, wave_bill_ids, verified) VALUES (643, 1470, 'THOMAS', 'REIMBURSEMENT', 'Thomas card payment (TRIANGLE) reimbursement.', NULL, 1);
DELETE FROM shareholder_transactions;
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (1, 377, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne - $20,000', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (2, 688, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne - $5,000', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (3, 1085, 'THOMAS', 'PAYROLL', 'Payroll to Thomas - $4,321.07', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (4, 1086, 'DWAYNE', 'LOAN_ISSUED', 'Shareholder loan to Dwayne - $9,000', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (5, 1090, 'CORP', 'DONATION', 'Donation to Relay for Life (Canadian Cancer Society) - $110.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (6, 1645, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 70)', '70', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (7, 1542, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 110)', '110', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (8, 1478, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 111)', '111', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (9, 1447, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 145)', '145', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (10, 1148, 'THOMAS', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 276)', '276', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (11, 1074, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 328)', '328', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (12, 782, 'UNKNOWN', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 495)', '495', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (13, 683, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 525)', '525', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (14, 1669, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $127.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (15, 1658, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $123.91 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (16, 1659, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1157.64 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (17, 1660, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $140.04 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (18, 1661, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $102.50 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (19, 1662, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $265.68 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (20, 1663, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $222.21', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (21, 1647, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $118.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (22, 1639, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $805.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (23, 1640, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Walmart - Bill (Sep 5, 2023 placeholder)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (24, 1641, 'DWAYNE', 'REIMBURSEMENT', 'Expense reimbursement (Wave bill 42)', '42', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (25, 1630, 'CORP', 'BANK_FEE', 'CIBC per-transfer fee (account not unlimited at the time)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (26, 1627, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $263.60', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (27, 1622, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $266.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (28, 1617, 'THOMAS', 'REIMBURSEMENT', 'Thomas reimbursement for: GFS - Bill (cash off books)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (29, 1618, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $222.59 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (30, 1615, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $862.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (31, 1612, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $170.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (32, 1566, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $266.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (33, 1568, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $200.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (34, 1569, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $95.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (35, 1572, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $104.10 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (36, 1576, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $538.75 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (37, 1546, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $310.03', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (38, 1536, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $88.80 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (39, 1524, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $352.29', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (40, 1525, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $95.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (41, 1526, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $265.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (42, 1508, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $85.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (43, 1509, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $271.40', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (44, 1510, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Maddison Troop - $59.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (45, 1511, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $264.97', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (46, 1503, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 1994069 (PDF; missed HST FY2024)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (47, 1504, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1437.22 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (48, 1498, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $170.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (49, 1487, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Maddison Troop - $77.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (50, 1488, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $211.95', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (51, 1485, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $372.67', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (52, 1477, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $116.87 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (53, 1465, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $159.96', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (54, 1448, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $72.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (55, 1449, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $194.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (56, 1450, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $36.50 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (57, 1451, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $148.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (58, 1452, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $100.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (59, 1444, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $473.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (60, 1446, 'UNKNOWN', 'DONATION', 'Sponsorship of kid''s hockey team/jersey (Tim Rich)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (61, 1438, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $146.10', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (62, 1430, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $495.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (63, 1431, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $2000.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (64, 1423, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $9.88 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (65, 1418, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $177.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (66, 1408, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $213.90 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (67, 1390, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $2000.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (68, 1382, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $862.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (69, 1380, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $592.18', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (70, 1364, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $101.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (71, 1365, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $1541.41 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (72, 1366, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $41.01', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (73, 1367, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $91.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (74, 1362, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $114.82', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (75, 1350, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $40.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (76, 1352, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $621.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (77, 1353, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $279.05', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (78, 1329, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $169.75', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (79, 1323, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $400.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (80, 1314, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $726.68', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (81, 1315, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $240.85', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (82, 1307, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $285.98', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (83, 1285, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $20.69 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (84, 1276, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-01', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (85, 1277, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $72.02 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (86, 1278, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $893.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (87, 1279, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $246.11', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (88, 1280, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (89, 1266, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $17.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (90, 1258, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $200.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (91, 1260, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $111.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (92, 1255, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $566.16 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (93, 1228, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1305.38', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (94, 1237, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $558.47 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (95, 1238, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.82', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (96, 1239, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $223.32', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (97, 1240, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $168.79', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (98, 1212, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $169.75', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (99, 1213, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $189.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (100, 1196, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $79.04', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (101, 1197, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1277.17', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (102, 1198, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $263.63', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (103, 1199, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $151.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (104, 1182, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT MARKIE B'' - $1311.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (105, 1178, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (106, 1179, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $49.09', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (107, 1163, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $1065.27', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (108, 1164, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (109, 1165, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $119.31', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (110, 1152, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $257.05', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (111, 1153, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $233.39', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (112, 1132, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $844.09', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (113, 1133, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $178.23', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (114, 1134, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $297.54', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (115, 1128, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT CHARLIE'' - $30.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (116, 1122, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-04', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (117, 1113, 'THOMAS', 'RENT_REIMBURSEMENT', 'Rent reimbursement to THOMAS - $402.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (118, 1114, 'THOMAS', 'RENT_REIMBURSEMENT', 'Rent reimbursement to THOMAS - $402.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (119, 1110, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $70.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (120, 1080, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $125.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (121, 1077, 'DWAYNE', 'RENT_REIMBURSEMENT', 'Rent reimbursement to DWAYNE - $402.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (122, 1071, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $18.56 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (123, 1063, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $105.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (124, 1064, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $95.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (125, 1051, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (126, 1060, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $81.83', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (127, 1061, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (128, 1042, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1282.50 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (129, 1043, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $68.86', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (130, 1044, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $265.82', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (131, 1045, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $307.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (132, 1036, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $412.29', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (133, 1026, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $134.68', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (134, 1027, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $201.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (135, 1028, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $77.51', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (136, 1029, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $78.84', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (137, 1003, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (138, 1004, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $409.97', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (139, 1005, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $198.09', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (140, 1006, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $142.85', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (141, 1007, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $64.43', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (142, 997, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $200.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (143, 998, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $100.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (144, 988, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $90.49', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (145, 989, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $318.40', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (146, 990, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (147, 991, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $259.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (148, 959, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $737.76', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (149, 960, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (150, 961, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $363.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (151, 962, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $178.40', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (152, 963, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $63.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (153, 965, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-09', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (154, 946, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $142.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (155, 947, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $116.42', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (156, 948, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $253.99', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (157, 949, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $202.83', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (158, 925, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $899.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (159, 926, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (160, 927, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $174.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (161, 928, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $421.48', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (162, 929, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $187.05', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (163, 909, 'THOMAS', 'HST_REIMBURSEMENT', 'HST reimbursement to THOMAS Q1 2025', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (164, 895, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $329.65', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (165, 896, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $349.43', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (166, 897, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $125.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (167, 898, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $191.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (168, 867, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $389.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (169, 868, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $886.31', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (170, 869, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $268.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (171, 870, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $240.85', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (172, 840, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $367.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (173, 845, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $31.44 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (174, 849, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $81.83', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (175, 850, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $212.51', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (176, 851, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $279.84', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (177, 817, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $93.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (178, 818, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $421.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (179, 826, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $176.96', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (180, 827, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $176.96', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (181, 828, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $258.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (182, 830, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $402.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (183, 814, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $779.21', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (184, 807, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $240.41', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (185, 808, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $181.77', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (186, 809, 'VENDOR', 'UNINVOICED_PAYMENT', 'Payment for stickers (uninvoiced) - $20.69', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (187, 802, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $63.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (188, 803, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $142.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (189, 791, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $909.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (190, 792, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $449.69', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (191, 793, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $274.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (192, 794, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $450.67', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (193, 777, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $254.74 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (194, 767, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to LIL'' EM''S - $46.00 (split for Wave bill 514)', '514', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (195, 768, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to LIL'' EM''S - $46.00 (split for Wave bill 514)', '514', 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (196, 770, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $50.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (197, 762, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1760.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (198, 748, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $279.84', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (199, 749, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $133.72', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (200, 750, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $282.48', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (201, 751, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $29.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (202, 752, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $226.38', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (203, 757, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $496.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (204, 731, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $642.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (205, 732, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $238.53', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (206, 733, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $380.85', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (207, 734, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $428.64', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (208, 735, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $309.90', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (209, 737, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT U9 DEV D'' - $200.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (210, 715, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $12.21 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (211, 716, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $400.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (212, 717, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $230.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (213, 718, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1500.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (214, 708, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $182.72', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (215, 709, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $142.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (216, 702, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (217, 703, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $73.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (218, 697, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $1500.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (219, 690, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $249.23', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (220, 691, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $196.22', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (221, 671, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $93.90', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (222, 672, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $50.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (223, 673, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $61.44', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (224, 674, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $230.95', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (225, 675, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $534.30', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (226, 676, 'THOMAS', 'OWNER_DRAW', 'Owner draw to Thomas - $1,000', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (227, 660, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $173.15', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (228, 661, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $242.35', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (229, 662, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $276.14', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (230, 663, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $366.92', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (231, 664, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $431.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (232, 641, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $500.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (233, 632, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $75.52', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (234, 633, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $75.52', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (235, 634, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $228.81', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (236, 635, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $201.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (237, 636, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $348.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (238, 637, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (239, 639, 'VENDOR', 'DUCKS_REVENUE_RETURN', 'Amherst Ducks ticket revenue return - $218.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (240, 611, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $166.01 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (241, 619, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $72.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (242, 620, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kaylee Gallagher - $72.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (243, 621, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $169.56', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (244, 622, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $319.65', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (245, 623, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $402.44', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (246, 624, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $370.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (247, 592, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $51.97', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (248, 593, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $56.30', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (249, 594, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $251.98', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (250, 595, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $328.14', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (251, 579, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $69.01', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (252, 580, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $170.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (253, 581, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $224.56', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (254, 582, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $375.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (255, 583, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $430.22', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (256, 546, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $277.27', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (257, 547, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $245.62', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (258, 548, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $357.30', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (259, 549, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $472.74', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (260, 535, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $87.80', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (261, 536, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $149.88', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (262, 537, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $144.65', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (263, 538, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $299.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (264, 539, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $290.18', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (265, 527, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $73.64 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (266, 506, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $79.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (267, 507, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $188.44', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (268, 508, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $201.01', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (269, 509, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $348.55', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (270, 489, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $181.69', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (271, 491, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $208.40', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (272, 492, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $99.44', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (273, 493, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $208.40', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (274, 494, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $342.24', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (275, 495, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $385.75', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (276, 482, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (277, 483, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $500.00 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (278, 476, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $81.38', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (279, 477, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $147.99', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (280, 478, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $299.05', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (281, 479, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $336.98', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (282, 435, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $172.41', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (283, 436, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $103.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (284, 437, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $219.04', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (285, 438, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $296.37', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (286, 419, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $73.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (287, 420, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $138.30', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (288, 421, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $152.99', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (289, 422, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $225.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (290, 408, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $118.54', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (291, 409, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $302.21', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (292, 410, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $180.86', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (293, 388, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $96.26', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (294, 389, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $319.15', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (295, 390, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $310.10', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (296, 384, 'THOMAS', 'PAYROLL_REIMBURSE', 'Payroll remittance reimbursement to THOMAS 2024-03', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (297, 378, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (298, 379, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $219.74', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (299, 380, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $249.14', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (300, 364, 'THOMAS', 'OWNER_DRAW', 'Owner draw to Thomas - $2,900', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (301, 365, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $80.89', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (302, 362, 'THOMAS', 'LOAN_ISSUED', 'Shareholder loan to Thomas - $2,000', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (303, 363, 'THOMAS', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to THOMAS - $610.15 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (304, 358, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $111.64', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (305, 351, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (306, 349, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (307, 329, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT AUCTIONS'' - $783.75', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (308, 327, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (309, 328, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $100.35', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (310, 324, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT TERRI'' - $100.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (311, 314, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (312, 304, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (313, 305, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Tyson Ogden - $64.63', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (314, 299, 'VENDOR', 'VENDOR_ETRANSFER', 'Amherst Ramblers - Marketing: logo on ice sponsorship - $1250.00', CAST((SELECT id FROM wave_bills WHERE invoice_number = 'RAMBLERS-LOGO-ICE-20250625' LIMIT 1) AS TEXT), 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (315, 300, 'VENDOR', 'VENDOR_ETRANSFER', 'Amherst Ramblers - Marketing: golf tournament sponsorship - $150.00', CAST((SELECT id FROM wave_bills WHERE invoice_number = 'RAMBLERS-GOLF-20250625' LIMIT 1) AS TEXT), 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (316, 296, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (317, 293, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (318, 294, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $50.64', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (319, 290, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (320, 288, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $34.02 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (321, 287, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (322, 284, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $134.71', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (323, 281, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $192.38', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (324, 275, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $203.90', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (325, 276, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $65.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (326, 274, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $127.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (327, 258, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $219.28', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (328, 259, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $88.58', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (329, 260, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $274.64', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (330, 255, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT DEAN TUP'' - $100.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (331, 248, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $104.55', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (332, 249, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $88.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (333, 250, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $218.18', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (334, 251, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $435.36', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (335, 252, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $614.17', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (336, 234, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $194.66', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (337, 235, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $134.08', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (338, 236, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $172.09', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (339, 224, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $60.67', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (340, 225, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $128.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (341, 226, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $342.11', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (342, 227, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $494.27', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (343, 209, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $175.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (344, 210, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $77.14', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (345, 211, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $227.61', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (346, 212, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $306.31', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (347, 213, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $448.11', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (348, 189, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $283.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (349, 190, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $132.59', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (350, 191, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $275.29', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (351, 192, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $405.19', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (352, 175, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT MATT SEL'' - $300.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (353, 176, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $154.70', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (354, 177, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $388.23', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (355, 178, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $213.10', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (356, 179, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $289.17', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (357, 180, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $388.81', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (358, 169, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to COVERED BRIDGE - $933.43 (needs Wave bill)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (359, 158, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $312.58', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (360, 159, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $490.65', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (361, 160, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $540.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (362, 161, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $571.76', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (363, 162, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $637.51', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (364, 130, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT AMHERST'' - $142.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (365, 113, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $192.26', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (366, 114, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $509.10', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (367, 115, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $335.82', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (368, 116, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $407.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (369, 117, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $552.45', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (370, 100, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $142.05', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (371, 101, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $455.97', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (372, 102, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $229.48', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (373, 103, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $470.07', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (374, 104, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $493.88', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (375, 87, 'VENDOR', 'VENDOR_ETRANSFER', 'Vendor payment to COVERED BRIDGE - $364.07 (needs Wave bill)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (376, 74, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $70.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (377, 75, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $364.73', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (378, 76, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $110.87', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (379, 77, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $333.34', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (380, 78, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $366.25', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (381, 80, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT'' - $132.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (382, 52, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $339.16', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (383, 53, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Mary Butcher - $168.71', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (384, 54, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $394.90', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (385, 55, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $238.02', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (386, 56, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $424.46', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (387, 57, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $492.35', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (388, 39, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Amanda Willet - $161.74', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (389, 40, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $423.42', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (390, 41, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $295.64', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (391, 42, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $363.61', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (392, 43, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $375.55', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (393, 12, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Amanda Willet - $74.47', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (394, 13, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kyler Edwards - $345.77', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (395, 14, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Kensie Atkinson - $199.98', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (396, 15, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Jesse Goodwin - $305.74', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (397, 16, 'EMPLOYEE', 'EMPLOYEE_PAYROLL', 'Employee payroll/tips to Anthony MacDonald - $332.12', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (398, 5, 'DWAYNE', 'SHAREHOLDER_UNMATCHED', 'Unmatched e-transfer to DWAYNE - $914.18 (needs invoice)', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (399, 3, 'UNKNOWN', 'UNKNOWN_ETRANSFER', 'Unknown e-transfer to ''ONE-TIME CONTACT JAMIE MA'' - $415.30', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (400, 10, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (401, 27, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2025-10', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (402, 28, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2025-09', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (403, 257, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (404, 279, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $42.57', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (405, 295, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (406, 298, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2999.56', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (407, 330, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $257.17', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (408, 338, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (409, 352, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $929.60', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (410, 360, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $4.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (411, 375, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $8231.53', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (412, 387, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $1240.32', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (413, 416, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $6.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (414, 458, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $27.29', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (415, 503, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $589.74', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (416, 504, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $772.79', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (417, 505, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (418, 568, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $796.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (419, 591, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (420, 657, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2572.87', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (421, 689, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (422, 761, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2289.89', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (423, 789, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $8.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (424, 798, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $2542.18', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (425, 834, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $3064.77', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (426, 835, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance - $3774.16', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (427, 862, 'CORP', 'PAYROLL_REMIT', 'CRA payroll remittance for 2024-10', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (428, 346, 'DWAYNE', 'OWNER_DRAW', 'Owner draw to Dwayne (transfer)', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (429, 540, 'CORP', 'INTERNAL_TRANSFER', 'Internal transfer - $5070.00', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (430, 1689, 'CORP', 'INTERNAL_TRANSFER', 'Internal transfer - $402.50', NULL, 0);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (431, 19, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (432, 105, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (433, 208, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (434, 269, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (435, 282, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (436, 297, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (437, 340, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (438, 345, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (439, 361, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (440, 418, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (441, 511, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (442, 533, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (443, 596, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (444, 696, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (445, 796, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (446, 879, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (447, 993, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (448, 1062, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (449, 1076, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (450, 1082, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (451, 1092, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (452, 1123, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (453, 1184, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (454, 1264, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (455, 1339, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (456, 1419, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (457, 1481, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (458, 1543, 'CORP', 'BANK_FEE', 'Bank service fee - $65.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (459, 1629, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (460, 1632, 'CORP', 'BANK_FEE', 'Bank service fee - $2.50', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (461, 1633, 'CORP', 'BANK_FEE', 'Bank service fee - $40.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (462, 1676, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (463, 1677, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (464, 1683, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (465, 1684, 'CORP', 'BANK_FEE', 'Bank service fee - $1.25', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (466, 1685, 'CORP', 'BANK_FEE', 'Bank service fee - $2.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (467, 1688, 'CORP', 'BANK_FEE', 'Bank service fee - $5.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (468, 1690, 'CORP', 'BANK_FEE', 'Bank service fee - $6.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (469, 1692, 'CORP', 'BANK_FEE', 'Bank service fee - $2.00', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (470, 1693, 'CORP', 'BANK_FEE', 'Bank service fee - $1.25', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (471, 383, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (473, 457, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (475, 487, 'CORP', 'VENDOR_PAYMENT', 'Sysco vendor payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (477, 512, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (478, 515, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (482, 551, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (483, 569, 'CORP', 'UTILITIES', 'Bell Aliant phone/internet', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (484, 597, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (485, 643, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (486, 655, 'CORP', 'INSURANCE', 'BFL Insurance payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (487, 684, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (488, 724, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (490, 781, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Walmart - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (491, 785, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Dollarama - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (492, 787, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (493, 790, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: GFS - Bill 9013824877', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (494, 816, 'CORP', 'EFT_PAYMENT', 'EFT misc payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (495, 880, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (496, 884, 'UNKNOWN', 'CASH_WITHDRAWAL', 'ATM/branch cash withdrawal', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (497, 894, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (499, 903, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (501, 935, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (502, 937, 'UNKNOWN', 'CASH_WITHDRAWAL', 'ATM/branch cash withdrawal', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (503, 953, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Shell Gas - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (504, 954, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 3110269', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (506, 1052, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Facebook Marketplace - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (507, 1057, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Atlantic Superstore - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (508, 1059, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 30000969', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (509, 1081, 'CORP', 'VENDOR_PAYMENT', 'Sysco vendor payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (510, 1106, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (511, 1109, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Bridge Workshop - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (512, 1131, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 25', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (513, 1143, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (514, 1151, 'CORP', 'PAYROLL_REMIT', 'EFT payroll/deduction remittance', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (515, 1185, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (516, 1211, 'CORP', 'EFT_PAYMENT', 'EFT misc payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (517, 1223, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2425069', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (518, 1224, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2437469', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (519, 1225, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Town of Amherst - Bill March Rent', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (520, 1243, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2423469', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (521, 1284, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2365969', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (522, 1286, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Jeff Bembridge - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (523, 1287, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Electric Kitty - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (524, 1324, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: GFS - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (525, 1351, 'THOMAS', 'REIMBURSEMENT', 'Thomas payment for: Town of Amherst - Bill FEbruary REnt', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (526, 1363, 'CORP', 'INSURANCE', 'BFL Insurance payment', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (527, 1396, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill 2220169', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (528, 1492, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Town of Amherst - Bill', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (529, 1521, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Curly''s Sports and Supplements - Bill D1', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (530, 1559, 'DWAYNE', 'REIMBURSEMENT', 'Reimbursement for: Mondoux - Bill 8100383', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (532, 1631, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (535, 1656, 'VENDOR', 'VENDOR_PAYMENT', 'Covered Bridge Chips vendor', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (541, 1691, 'CORP', 'BANK_FEE', 'CIBC account fee', NULL, 1);
INSERT INTO shareholder_transactions (id, bank_txn_id, shareholder, txn_category, explanation, wave_bill_ids, verified) VALUES (542, 347, 'DWAYNE', 'LOAN_REPAID', 'Loan repaid by Dwayne (transfer)', NULL, 1);
DELETE FROM cc_payment_links;
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (1, 1637, 4116, 9254, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (2, 1638, 4117, 121536, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (3, 1642, 4118, 234693, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (4, 1643, 4119, 112951, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (5, 1601, 4086, 8249, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (6, 1602, 4087, 6254, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (7, 1603, 4088, 22407, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (8, 1604, 1551, 2996, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (9, 1605, 4083, 85132, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (10, 1606, 4085, 4827, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (11, 1607, 4084, 23673, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (12, 1608, 1552, 10193, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (13, 1564, 4066, 6254, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (14, 1565, 4067, 99488, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (15, 1570, 1533, 10740, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (16, 1571, 1532, 8437, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (17, 1573, 4077, 5635, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (18, 1574, 4078, 4018, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (19, 1575, 4076, 3771, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (20, 1577, 1536, 30397, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (21, 1578, 1535, 5175, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (22, 1579, 1537, 2561, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (23, 1580, 4079, 58238, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (24, 1581, 1534, 64363, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (25, 1582, 4070, 152352, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (26, 1583, 4071, 7010, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (27, 1584, 1540, 613, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (28, 1585, 1541, 2831, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (29, 1586, 1543, 2607, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (30, 1587, 1542, 1734, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (31, 1588, 4072, 13790, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (32, 1589, 1538, 2644, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (33, 1590, 1539, 2532, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (34, 1591, 4074, 1954, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (35, 1592, 1544, 2995, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (36, 1593, 1545, 1954, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (37, 1594, 1546, 2995, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (38, 1595, 4073, 5913, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (39, 1596, 4075, 16785, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (40, 1597, 4069, 1024, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (41, 1598, 1547, 5216, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (42, 1563, 4065, 7883, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (43, 1557, 1519, 3819, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (44, 1558, 1518, 574, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (45, 1560, 4063, 137182, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (46, 1554, 1513, 4022, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (47, 1547, 1509, 9159, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (48, 1548, 4057, 6404, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (49, 1549, 1507, 4599, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (50, 1550, 1506, 4082, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (51, 1551, 4056, 58657, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (52, 1537, 4054, 197798, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (53, 1538, 1497, 859, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (54, 1539, 4055, 63181, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (55, 1540, 1498, 194291, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (56, 1533, 1489, 6832, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (57, 1534, 1491, 18442, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (58, 1535, 1490, 715, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (59, 1529, 1483, 7601, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (60, 1530, 1486, 18539, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (61, 1516, 4049, 13800, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (62, 1517, 1464, 92900, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (63, 1518, 1466, 11092, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (64, 1519, 1468, 5749, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (65, 1520, 4048, 136617, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (66, 1506, 4037, 6356, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (67, 1494, 4022, 165922, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (68, 1489, 1434, 14249, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (69, 1482, 4002, 15899, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (70, 1483, 4001, 1148, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (71, 1469, 3999, 212938, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (72, 1471, 3998, 4658, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (73, 1472, 1419, 8212, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (74, 1473, 1418, 1161, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (75, 1474, 1417, 28163, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (76, 1475, 1421, 6782, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (77, 1476, 3997, 6695, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (78, 1466, 3989, 3131, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (79, 1458, 3981, 3562, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (80, 1459, 1413, 3608, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (81, 1460, 3980, 119488, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (82, 1455, 1410, 19237, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (83, 1437, 3953, 121236, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (84, 1421, 1387, 2636, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (85, 1422, 1385, 2868, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (86, 1424, 1386, 4181, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (87, 1426, 1388, 26537, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (88, 1409, 1371, 2753, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (89, 1410, 1370, 1432, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (90, 1411, 1369, 3366, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (91, 1412, 1372, 10254, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (92, 1413, 3931, 3560, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (93, 1414, 1375, 4342, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (94, 1415, 1374, 4887, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (95, 1416, 1373, 2753, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (96, 1398, 1353, 3842, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (97, 1399, 3917, 199638, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (98, 1401, 3921, 7414, '154', 0);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (99, 1402, 1365, 29230, '318', 0);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (100, 1403, 3920, 2010, '154', 0);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (101, 1404, 1366, 2010, '318', 0);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (102, 1393, 1352, 3987, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (103, 1394, 3913, 3449, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (104, 1395, 3914, 2299, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (105, 1387, 1348, 5876, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (106, 1388, 1349, 19237, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (107, 1391, 1350, 28865, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (108, 1378, 3903, 8497, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (109, 1379, 3902, 3999, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (110, 1368, 1333, 6375, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (111, 1369, 1334, 2892, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (112, 1370, 1331, 10403, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (113, 1371, 1332, 5449, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (114, 1372, 1330, 738, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (115, 1343, 1305, 5352, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (116, 1344, 1307, 1179, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (117, 1345, 1306, 1107, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (118, 1346, 1303, 3013, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (119, 1347, 3879, 148980, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (120, 1348, 1302, 2588, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (121, 1349, 1304, 4823, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (122, 1341, 3877, 152197, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (123, 1333, 1296, 6780, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (124, 1334, 3871, 4001, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (125, 1335, 3870, 187393, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (126, 1336, 1299, 14038, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (127, 1337, 1297, 43474, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (128, 1325, 1290, 8203, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (129, 1326, 1291, 20593, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (130, 1318, 3859, 24971, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (131, 1288, 1246, 5130, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (132, 1289, 1245, 11982, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (133, 1292, 3844, 224931, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (134, 1293, 1247, 1300, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (135, 1295, 1248, 10554, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (136, 1298, 1250, 5996, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (137, 1299, 1249, 1147, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (138, 1300, 1251, 3619, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (139, 1302, 1244, 96143, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (140, 1270, 1232, 5988, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (141, 1271, 1231, 2995, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (142, 1272, 3838, 9897, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (143, 1274, 1230, 4796, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (144, 1275, 1229, 38101, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (145, 1268, 3833, 166598, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (146, 1249, 1210, 1207, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (147, 1250, 1211, 4352, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (148, 1252, 1209, 2130, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (149, 1254, 3810, 123876, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (150, 1235, 1203, 2194, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (151, 1236, 3806, 14362, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (152, 1216, 3800, 63249, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (153, 1217, 3801, 4595, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (154, 1219, 3796, 161259, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (155, 1204, 1184, 5421, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (156, 1205, 1182, 4383, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (157, 1206, 1183, 22743, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (158, 1207, 1181, 18239, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (159, 1208, 1180, 13328, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (160, 1193, 1168, 4118, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (161, 1194, 1167, 23656, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (162, 1195, 3775, 132574, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (163, 1174, 3760, 81189, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (164, 1175, 3758, 125173, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (165, 1167, 3754, 20378, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (166, 1168, 3753, 10735, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (167, 1169, 3752, 1995, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (168, 1155, 3734, 2743, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (169, 1156, 3733, 1446, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (170, 1157, 3738, 66747, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (171, 1158, 3737, 16862, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (172, 1144, 1132, 13611, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (173, 1145, 1131, 2988, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (174, 1146, 1134, 3515, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (175, 1147, 1133, 23121, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (176, 1135, 1119, 6549, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (177, 1136, 1120, 2892, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (178, 1137, 1121, 9492, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (179, 1127, 1118, 22259, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (180, 1124, 1100, 12818, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (181, 1118, 1089, 20989, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (182, 1119, 1088, 6328, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (183, 1120, 1087, 1990, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (184, 1115, 1085, 2008, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (185, 1116, 3699, 3194, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (186, 1117, 3697, 6284, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (187, 1111, 3692, 85830, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (188, 1102, 1048, 8727, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (189, 1103, 1049, 6514, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (190, 1104, 1050, 7111, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (191, 1097, 1035, 2964, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (192, 1098, 3673, 8086, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (193, 1096, 1032, 28865, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (194, 1093, 1022, 3481, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (195, 1094, 1023, 21352, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (196, 1079, 957, 2978, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (197, 1072, 903, 13555, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (198, 1073, 905, 1401, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (199, 1066, 886, 10178, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (200, 1067, 885, 23789, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (201, 1068, 3547, 108039, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (202, 1053, 3517, 13054, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (203, 1054, 864, 4053, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (204, 1056, 3518, 139042, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (205, 1049, 3513, 33640, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (206, 1039, 3503, 1442, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (207, 1040, 3502, 3845, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (208, 1020, 3480, 32165, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (209, 1021, 3479, 24844, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (210, 1022, 3481, 15935, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (211, 1023, 843, 3044, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (212, 1024, 3482, 6303, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (213, 1009, 3474, 33442, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (214, 995, 3465, 178197, '154', 4);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (215, 996, 3466, 111445, '154', 4);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (216, 980, 3452, 80755, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (217, 982, 3451, 35522, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (218, 985, 3453, 13054, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (219, 986, 3454, 9198, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (220, 975, 3442, 5633, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (221, 966, 3426, 208323, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (222, 967, 3427, 1576, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (223, 968, 3428, 93233, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (224, 971, 3424, 27541, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (225, 951, 3414, 4955, '154', 4);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (226, 952, 810, 53107, '318', 4);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (227, 945, 3408, 13041, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (228, 920, 3396, 186909, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (229, 921, 3395, 32288, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (230, 924, 3394, 29471, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (231, 918, 3392, 23691, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (232, 906, 3386, 147283, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (233, 887, 3377, 47932, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (234, 889, 778, 9302, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (235, 891, 3378, 7830, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (236, 892, 3379, 2200, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (237, 865, 769, 27478, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (238, 866, 768, 10590, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (239, 872, 3366, 3223, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (240, 873, 771, 62763, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (241, 874, 3365, 167289, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (242, 858, 762, 3274, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (243, 839, 3350, 55087, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (244, 841, 743, 57059, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (245, 842, 3354, 6203, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (246, 844, 3352, 10626, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (247, 846, 3353, 27908, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (248, 821, 3333, 109096, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (249, 822, 3337, 25176, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (250, 823, 736, 8984, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (251, 824, 3336, 178776, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (252, 771, 3296, 25812, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (253, 773, 3300, 1678, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (254, 774, 3299, 6288, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (255, 775, 3298, 36859, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (256, 778, 3297, 40000, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (257, 779, 717, 3002, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (258, 780, 3295, 2466, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (259, 783, 3293, 21846, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (260, 784, 3294, 2476, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (261, 786, 716, 6498, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (262, 753, 3262, 27981, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (263, 754, 3263, 3777, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (264, 756, 3261, 28348, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (265, 744, 3255, 11897, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (266, 745, 3256, 7579, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (267, 740, 705, 68884, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (268, 726, 3225, 8335, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (269, 729, 3226, 3051, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (270, 713, 3211, 215203, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (271, 714, 3210, 40000, '154', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (272, 698, 3184, 6395, '154', 2);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (273, 699, 3183, 1724, '154', 2);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (274, 677, 3164, 10840, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (275, 678, 3163, 5586, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (276, 679, 676, 69166, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (277, 680, 3162, 4816, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (278, 681, 3161, 7622, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (279, 644, 662, 2921, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (280, 645, 3135, 1440, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (281, 646, 660, 40710, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (282, 647, 3140, 9008, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (283, 648, 3138, 241547, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (284, 649, 3139, 3600, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (285, 650, 3137, 12929, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (286, 652, 3136, 64289, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (287, 653, 3141, 33747, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (288, 654, 661, 34067, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (289, 605, 3110, 7970, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (290, 606, 3111, 7691, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (291, 608, 3107, 4218, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (292, 609, 3109, 6000, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (293, 610, 3108, 12189, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (294, 612, 3106, 40000, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (295, 613, 639, 2800, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (296, 614, 634, 18503, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (297, 615, 636, 14615, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (298, 616, 635, 22883, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (299, 617, 638, 9090, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (300, 618, 637, 1640, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (301, 576, 590, 4074, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (302, 577, 588, 3679, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (303, 578, 589, 7222, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (304, 555, 572, 60167, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (305, 556, 573, 32965, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (306, 557, 3065, 439125, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (307, 558, 3064, 231434, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (308, 559, 574, 15541, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (309, 560, 575, 2101, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (310, 562, 576, 103368, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (311, 564, 3063, 11904, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (312, 565, 3062, 1169, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (313, 516, 529, 63228, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (314, 519, 3032, 195820, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (315, 520, 528, 19324, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (316, 523, 533, 2625, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (317, 524, 534, 4927, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (318, 525, 535, 12986, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (319, 526, 536, 1561, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (320, 528, 537, 28200, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (321, 501, 521, 41283, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (322, 459, 491, 5862, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (323, 460, 490, 3792, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (324, 461, 489, 1954, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (325, 462, 492, 19545, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (326, 464, 486, 11086, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (327, 466, 485, 8008, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (328, 468, 2987, 186991, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (329, 469, 493, 2760, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (330, 470, 496, 2181, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (331, 471, 495, 6617, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (332, 472, 494, 30531, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (333, 475, 487, 4495, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (334, 453, 479, 15707, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (335, 454, 480, 123686, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (336, 442, 464, 12068, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (337, 443, 470, 1264, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (338, 444, 469, 2068, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (339, 446, 472, 3449, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (340, 447, 471, 11658, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (341, 448, 2980, 253183, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (342, 449, 465, 16628, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (343, 450, 466, 68218, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (344, 428, 453, 5952, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (345, 429, 449, 9302, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (346, 430, 450, 892, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (347, 431, 451, 9719, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (348, 404, 434, 7226, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (349, 406, 435, 6855, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (350, 393, 422, 13268, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (351, 394, 423, 13268, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (352, 395, 421, 13153, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (353, 396, 426, 13268, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (354, 397, 427, 13268, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (355, 366, 404, 1945, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (356, 368, 403, 33391, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (357, 369, 405, 2783, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (358, 371, 406, 12194, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (359, 372, 402, 4599, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (360, 354, 389, 4903, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (361, 355, 390, 5070, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (362, 356, 391, 5108, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (363, 357, 393, 5107, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (364, 350, 384, 40858, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (365, 334, 362, 4574, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (366, 335, 360, 3217, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (367, 336, 361, 3217, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (368, 337, 2796, 6202, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (369, 317, 330, 5173, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (370, 318, 327, 3902, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (371, 319, 328, 3902, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (372, 320, 2751, 4766, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (373, 321, 331, 3419, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (374, 322, 326, 25606, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (375, 313, 2748, 14921, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (376, 307, 2736, 4792, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (377, 308, 324, 4912, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (378, 311, 323, 3889, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (379, 292, 300, 22994, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (380, 286, 271, 28621, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (381, 283, 259, 8739, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (382, 262, 2522, 7155, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (383, 263, 2523, 4896, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (384, 264, 225, 2460, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (385, 265, 228, 8739, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (386, 268, 2524, 2168, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (387, 246, 2502, 18624, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (388, 242, 2498, 7277, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (389, 243, 2499, 347132, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (390, 223, 193, 66698, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (391, 216, 188, 68138, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (392, 217, 187, 25680, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (393, 202, 2448, 5794, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (394, 206, 177, 17099, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (395, 207, 179, 36140, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (396, 196, 2439, 313137, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (397, 197, 2438, 288295, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (398, 198, 174, 63496, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (399, 185, 2421, 547947, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (400, 133, 116, 11792, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (401, 134, 117, 6952, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (402, 135, 118, 3197, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (403, 137, 122, 30424, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (404, 138, 121, 6875, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (405, 139, 120, 18153, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (406, 140, 119, 3419, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (407, 141, 134, 70384, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (408, 143, 128, 46234, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (409, 144, 127, 17400, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (410, 145, 126, 5558, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (411, 146, 125, 4823, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (412, 147, 124, 4914, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (413, 148, 123, 147409, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (414, 149, 130, 20403, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (415, 151, 129, 3264, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (416, 154, 132, 3564, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (417, 155, 133, 9296, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (418, 156, 2384, 18964, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (419, 157, 131, 11915, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (420, 126, 2373, 191577, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (421, 127, 2374, 350360, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (422, 120, 99, 1420, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (423, 121, 97, 64232, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (424, 122, 105, 34816, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (425, 123, 98, 5558, '318', 3);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (426, 112, 95, 36140, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (427, 91, 76, 2081, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (428, 92, 75, 5130, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (429, 93, 74, 25362, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (430, 95, 72, 41094, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (431, 96, 71, 25360, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (432, 97, 73, 5128, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (433, 98, 70, 36000, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (434, 64, 50, 11418, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (435, 65, 49, 2972, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (436, 66, 52, 4820, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (437, 67, 51, 53072, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (438, 68, 2291, 39901, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (439, 70, 48, 50773, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (440, 29, 27, 14280, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (441, 30, 26, 1689, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (442, 31, 28, 52860, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (443, 32, 2239, 69374, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (444, 33, 2241, 2352, '154', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (445, 34, 25, 20345, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (446, 35, 23, 9609, '318', 1);
INSERT INTO cc_payment_links (id, bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days) VALUES (447, 36, 24, 5194, '318', 1);
DELETE FROM pad_invoices;
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (1, 63, '2542817', 93890, NULL);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (2, 66, '2554160', 80612, 278);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (3, 68, '2580163', 40802, 339);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (4, 62, '2536709', 91733, 144);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (5, 67, '2560110', 17995, 312);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (6, 65, '2550997', 54052, 258);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (7, 76, '2548372', 89436, NULL);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (8, 64, '2549756', 26913, 239);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (9, 19, '9005873404', 97709, 164);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (13, 20, '9006132497', 60146, 171);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (14, 11, '9004423490', 55960, 122);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (15, 23, '9006727793', 107190, 204);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (16, 21, '9006467889', 93305, 188);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (17, 26, '9007568865', 62355, 249);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (18, 26, '9007669356', 64561, 253);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (19, 26, '9007713769', 28028, 254);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (20, 26, '9007763983', 34728, 263);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (25, 12, '9004638160', 96645, 127);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (26, 12, '9004686201', 25354, 129);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (27, 8, '9003993508', 83481, 96);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (28, 5, '9003665333', 60503, 73);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (29, 10, '9004259902', 88092, 115);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (30, 10, '9004290341', 42085, 117);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (31, 10, '9004309092', 14495, 116);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (32, 18, '9005827880', 68371, 159);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (33, 13, '9004838078', 62755, 132);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (34, 15, '9005163888', 93692, 141);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (35, 15, '9005216555', 46453, 142);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (36, 14, '9005011016', 45254, 137);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (37, 25, '9007456012', 87930, 243);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (38, 25, '9007510570', 5057, 245);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (39, 3, '9003386079', 24457, 48);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (40, 3, '9003462485', 27323, 55);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (41, 3, '9003468379', 80876, 56);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (42, 9, '9004092329', 4859, 105);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (43, 9, '9004106655', 85957, 107);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (44, 9, '9004135560', 43027, 109);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (45, 7, '9003882687', 85831, 87);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (46, 4, '9003552766', 6677, 63);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (47, 4, '9003558293', 97396, 62);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (48, 16, '9005299395', 63072, 146);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (49, 16, '9005357713', 155701, 147);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (52, 24, '9007262291', 84378, 233);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (53, 6, '9003775625', 99848, 79);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (54, 27, '9008498481', 119253, 286);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (55, 27, '9008642890', 95899, 291);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (56, 22, '9006623852', 46712, 193);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (57, 22, '9006683806', 10343, 198);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (61, 17, '9005693526', 40934, 150);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (62, 2, '9003327039', 104634, 43);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (63, 29, '9009454598', 38089, 305);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (64, 29, '9009517084', 38089, 304);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (65, 30, '9009641376', 89103, 313);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (66, 28, '9008934047', 28563, 297);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (67, 32, '9012713784', 12312, 330);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (70, 34, '9013663225', 40280, 352);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (71, 34, '9013664381', 15879, 351);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (72, 33, '9013501649', 45207, 342);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (73, 36, '9014096231', 48132, 369);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (74, 36, '9014294880', 66365, 375);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (75, 35, '9013824877', 13152, 358);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (76, 35, '9013837326', 61625, 363);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (77, 35, '9014036877', 15764, 366);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (78, 39, '9014962246', 78939, 412);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (79, 39, '9015055269', 46951, 418);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (80, 43, '9016098857', 79374, 472);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (81, 43, '9016122014', 6397, 471);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (82, 43, '9016230977', 92656, 479);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (83, 41, '9015806407', 85783, 460);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (84, 41, '9015806844', 6911, 459);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (85, 40, '9015111433', 96158, 420);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (86, 40, '9015204709', 38552, 423);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (87, 40, '9015302439', 60957, 429);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (88, 37, '9014383591', 51940, 382);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (89, 37, '9014406188', 9091, 383);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (90, 37, '9014549646', 20020, 393);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (94, 46, '9016950083', 155470, 517);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (95, 46, '9017022468', 53092, 518);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (96, 42, '9015983805', 137572, 465);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (97, 38, '9014589017', 90312, 399);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (98, 38, '9014609851', 12084, 398);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (99, 38, '9014750800', 57063, 403);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (100, 38, '9014783184', 28305, 402);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (101, 50, '9018093147', 114776, 562);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (102, 50, '9018118048', 44544, 563);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (103, 48, '9017524422', 46643, 540);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (104, 31, '9010616469', 5020, 320);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (105, 51, '9018308927', 57056, 572);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (106, 51, '9018338730', 58861, 573);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (107, 51, '9018356757', 14211, 574);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (108, 49, '9017785533', 36319, 546);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (109, 49, '9017847614', 92546, 548);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (110, 55, '9019510794', 88723, NULL);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (111, 44, '9016490855', 99331, 484);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (112, 44, '9016564992', 20020, 485);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (113, 47, '9017091772', 21962, 521);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (114, 47, '9017258411', 94431, 529);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (115, 53, '9018826421', 132273, 595);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (116, 52, '9018587030', 69568, 584);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (117, 52, '9018628162', 23704, 585);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (118, 54, '9019024514', 24547, 605);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (119, 45, '9016753711', 127503, 497);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (122, 57, '9020315231', 94764, 654);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (123, 56, '9019803957', 64576, NULL);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (124, 58, '9020484316', 97762, 668);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (127, 60, '9022611886', 22714, 701);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (135, 61, '9023101066', 16357, 704);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (136, 59, '9020622999', 87094, 672);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (137, 79, '9006903547', 21588, 220);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (138, 79, '9006903744', 135781, 216);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (139, 79, '9007010687', 35019, 222);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (140, 79, '9007044619', 5949, 224);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (141, 80, '9006298062', 87739, 182);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (142, 81, '9008171261', 126391, 274);
INSERT INTO pad_invoices (id, pad_payment_id, invoice_number, amount_cents, wave_bill_id) VALUES (143, 82, '9007911798', 79112, 266);
DELETE FROM pad_payments;
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (1, 1665, 'GFS', '2023-09-15', 36318, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (2, 1651, 'GFS', '2023-09-22', 104634, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (3, 1634, 'GFS', '2023-09-29', 132656, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (4, 1623, 'GFS', '2023-10-06', 104073, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (5, 1614, 'GFS', '2023-10-13', 60503, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (6, 1600, 'GFS', '2023-10-20', 99848, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (7, 1553, 'GFS', '2023-10-27', 85831, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (8, 1528, 'GFS', '2023-11-03', 83481, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (9, 1513, 'GFS', '2023-11-10', 133843, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (10, 1500, 'GFS', '2023-11-17', 144672, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (11, 1491, 'GFS', '2023-11-24', 55960, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (12, 1468, 'GFS', '2023-12-01', 121999, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (13, 1454, 'GFS', '2023-12-08', 62755, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (14, 1441, 'GFS', '2023-12-15', 45254, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (15, 1433, 'GFS', '2023-12-22', 140145, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (16, 1420, 'GFS', '2023-12-29', 218773, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (17, 1384, 'GFS', '2024-01-12', 40934, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (18, 1374, 'GFS', '2024-01-19', 68371, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (19, 1357, 'GFS', '2024-01-26', 97709, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (20, 1331, 'GFS', '2024-02-02', 60146, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (21, 1309, 'GFS', '2024-02-16', 93305, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (22, 1282, 'GFS', '2024-02-23', 57055, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (23, 1262, 'GFS', '2024-03-01', 107190, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (24, 1214, 'GFS', '2024-03-15', 84378, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (25, 1201, 'GFS', '2024-03-22', 92987, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (26, 1181, 'GFS', '2024-04-01', 189672, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (27, 1125, 'GFS', '2024-04-26', 215152, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (28, 1121, 'GFS', '2024-05-03', 28563, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (29, 1105, 'GFS', '2024-05-17', 76178, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (30, 1099, 'GFS', '2024-05-24', 89103, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (31, 1083, 'GFS', '2024-06-21', 5020, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (32, 1065, 'GFS', '2024-08-23', 12312, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (33, 1031, 'GFS', '2024-09-13', 45207, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (34, 1011, 'GFS', '2024-09-20', 56159, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (35, 994, 'GFS', '2024-09-27', 90541, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (36, 972, 'GFS', '2024-10-04', 114497, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (37, 950, 'GFS', '2024-10-11', 81051, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (38, 931, 'GFS', '2024-10-18', 187764, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (39, 900, 'GFS', '2024-10-25', 125890, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (40, 877, 'GFS', '2024-11-01', 195667, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (41, 831, 'GFS', '2024-11-15', 92694, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (42, 810, 'GFS', '2024-11-22', 137572, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (43, 797, 'GFS', '2024-11-29', 178427, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (44, 759, 'GFS', '2024-12-06', 119351, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (45, 738, 'GFS', '2024-12-13', 127503, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (46, 711, 'GFS', '2024-12-20', 208562, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (47, 705, 'GFS', '2024-12-27', 116393, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (48, 692, 'GFS', '2025-01-03', 46643, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (49, 640, 'GFS', '2025-01-17', 128865, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (50, 626, 'GFS', '2025-01-24', 159320, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (51, 598, 'GFS', '2025-01-31', 130128, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (52, 585, 'GFS', '2025-02-07', 93272, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (53, 552, 'GFS', '2025-02-14', 132273, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (54, 543, 'GFS', '2025-02-21', 24547, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (55, 497, 'GFS', '2025-03-07', 88723, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (56, 481, 'GFS', '2025-03-14', 64576, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (57, 424, 'GFS', '2025-03-28', 94764, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (58, 412, 'GFS', '2025-04-04', 97762, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (59, 392, 'GFS', '2025-04-11', 87094, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (60, 341, 'GFS', '2025-05-30', 22714, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (61, 323, 'GFS', '2025-06-13', 16357, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (62, 1428, 'CAPITAL', '2023-12-27', 91733, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (63, 1322, 'CAPITAL', '2024-02-07', 93890, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (64, 1203, 'CAPITAL', '2024-03-20', 26913, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (65, 1187, 'CAPITAL', '2024-03-27', 54052, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (66, 1141, 'CAPITAL', '2024-04-17', 80612, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (67, 1100, 'CAPITAL', '2024-05-22', 17995, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (68, 1034, 'CAPITAL', '2024-09-11', 40802, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (69, 936, 'CAPITAL', '2024-10-16', 129047, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (70, 882, 'CAPITAL', '2024-10-30', 33604, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (71, 801, 'CAPITAL', '2024-11-27', 229195, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (72, 670, 'CAPITAL', '2025-01-08', 162525, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (73, 601, 'CAPITAL', '2025-01-29', 82951, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (74, 500, 'CAPITAL', '2025-03-05', 125074, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (75, 427, 'CAPITAL', '2025-03-26', 111097, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (76, 1221, 'CAPITAL', '2024-03-13', 89436, 'Capital Foodservice PAP Emails/2024-03-11_Capital Foodservice PAP Payment for CUR300 14587430 CANADA INC_18e2dcb66370c1e0.html');
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (77, 588, 'CAPITAL', '2025-02-05', 100396, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (78, 400, 'CAPITAL', '2025-04-09', 147206, NULL);
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (79, 1242, 'GFS', '2024-03-08', 198337, 'EFT Notification_10.XLS (4 invoices)');
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (80, 1320, 'GFS', '2024-02-09', 139133, 'EFT Notification_14.XLS (3 invoices)');
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (81, 1154, 'GFS', '2024-04-12', 121334, 'EFT Notification_5.XLS (2 invoices)');
INSERT INTO pad_payments (id, bank_txn_id, vendor, payment_date, total_cents, source_pdf) VALUES (82, 1171, 'GFS', '2024-04-05', 183554, 'EFT Notification_7.XLS (3 invoices)');
DELETE FROM manual_receipts;
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (1, NULL, 'MANUAL-ETR-1128', 'corp', 'ONE-TIME CONTACT CHARLIE', '2024-04-23', 3000, 0, 3000, 'CAD', NULL, NULL, 'E_TRANSFER', 'manual', 'pending', 'Facebook Marketplace Merchanising Equipment | Price gun/stickers/clothes tagger auction win', '{"source": "review_unknown_etransfers.md", "description": "Internet Banking E-TRANSFER104967044962 One-time contact Charlie 4506*********695"}', 1128, NULL, NULL, 0, '2026-01-02 00:57:43', '2026-01-02 00:57:43');
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (2, NULL, 'MANUAL-ETR-767', 'corp', 'LIL'' EM''S', '2024-12-04', 4600, 0, 4600, 'CAD', NULL, NULL, 'E_TRANSFER', 'manual', 'pending', 'Pies for sale | Cost of goods sold baked goods', '{"source": "review_unknown_etransfers.md", "description": "Internet Banking E-TRANSFER105248068962 Lil'' Em''s 4506*********695"}', 767, NULL, NULL, 0, '2026-01-02 00:57:43', '2026-01-02 00:57:43');
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (3, NULL, 'MANUAL-ETR-768', 'corp', 'LIL'' EM''S', '2024-12-04', 4600, 0, 4600, 'CAD', NULL, NULL, 'E_TRANSFER', 'manual', 'pending', 'pies for sale. | Cost of goods sold baked goods', '{"source": "review_unknown_etransfers.md", "description": "Internet Banking E-TRANSFER105248068727 Lil'' Em''s 4506*********695"}', 768, NULL, NULL, 0, '2026-01-02 00:57:43', '2026-01-02 00:57:43');
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (4, NULL, 'MANUAL-CAP-2542817', 'corp', 'CAPITAL', '2024-02-07', 93890, 0, 93890, 'CAD', '2542817', NULL, 'PAD', 'manual', 'pending', 'PAP email (invoice date unknown)', '{"source": "capital_pap_email", "email_file": "Capital Foodservice PAP Emails/2024-02-06_Capital Foodservice PAP Payment for CUR300 14587430 CANADA INC_18d7fac6c7426f50.html"}', 1322, NULL, NULL, 0, '2026-01-02 00:57:44', '2026-01-02 00:57:44');
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (5, NULL, 'MANUAL-CAP-2548372', 'corp', 'CAPITAL', '2024-03-13', 89436, 0, 89436, 'CAD', '2548372', NULL, 'PAD', 'manual', 'pending', 'PAP email (invoice date unknown)', '{"source": "capital_pap_email", "email_file": "Capital Foodservice PAP Emails/2024-03-11_Capital Foodservice PAP Payment for CUR300 14587430 CANADA INC_18e2dcb66370c1e0.html"}', 1221, NULL, NULL, 0, '2026-01-02 00:57:44', '2026-01-02 00:57:44');
INSERT INTO manual_receipts (id, receipt_uuid, receipt_number, entity, vendor, receipt_date, subtotal_cents, tax_cents, total_cents, currency, invoice_number, original_file_path, payment_method, source, status, notes, metadata_json, matched_bank_txn_id, paid_by_name, paid_by_card_last4, requires_reimbursement, created_at, updated_at) VALUES (6, NULL, '1994069', 'corp', 'Curly''s Sports & Supplements', '2023-11-16', 101828, 15274, 117102, 'CAD', '1994069', '/home/clarencehub/Fresh/dump/Curly''s Sports & Supplements · Order #1994069 · Shopify.pdf', 'E-TRANSFER', 'manual', 'pending', 'Order #1994069 from PDF; missed in HST FY2024', '{"source_file": "/home/clarencehub/Fresh/dump/Curly''s Sports & Supplements \u00b7 Order #1994069 \u00b7 Shopify.pdf", "note": "Order printer export"}', 1503, NULL, NULL, 0, '2026-01-02 19:23:11', '2026-01-02 19:23:11');
-- Bank transaction flags (used/manual_classification/notes)
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 3;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 5;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 10;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 12;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 13;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 14;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 15;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 16;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 19;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 27;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 28;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 29;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 30;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 31;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 32;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 33;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 34;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 35;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 36;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 39;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 40;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 41;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 42;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 43;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 52;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 53;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 54;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 55;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 56;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 57;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 64;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 65;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 66;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 67;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 68;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 70;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 74;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 75;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 76;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 77;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 78;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 80;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 87;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 91;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 92;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 93;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 95;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 96;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 97;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 98;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 100;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 101;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 102;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 103;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 104;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 105;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 112;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 113;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 114;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 115;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 116;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 117;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 120;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 121;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 122;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 123;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 126;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 127;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 130;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 133;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 134;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 135;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 137;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 138;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 139;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 140;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 141;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 143;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 144;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 145;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 146;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 147;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 148;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 149;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 151;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 154;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 155;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 156;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 157;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 158;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 159;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 160;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 161;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 162;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 169;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 175;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 176;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 177;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 178;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 179;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 180;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 185;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 189;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 190;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 191;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 192;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 196;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 197;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 198;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 202;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 206;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 207;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 208;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kensie Atkinson' WHERE id = 209;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 210;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 211;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 212;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 213;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 216;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 217;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 223;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 224;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 225;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 226;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 227;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 234;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 235;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 236;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 242;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 243;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 246;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 248;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher' WHERE id = 249;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 250;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 251;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 252;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 255;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 257;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 258;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin' WHERE id = 259;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 260;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 262;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 263;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 264;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 265;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 268;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 269;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 274;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 275;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 276;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 279;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 281;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 282;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 283;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 284;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 286;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 287;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 288;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 290;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 292;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 293;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald' WHERE id = 294;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 295;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 296;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 297;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 298;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 299;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 300;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 304;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden' WHERE id = 305;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 307;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 308;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 309;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 311;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 312;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 313;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 314;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 315;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 316;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 317;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 318;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 319;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 320;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 321;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 322;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 323;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 324;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards' WHERE id = 327;
UPDATE bank_transactions SET used = 0, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden' WHERE id = 328;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 329;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 330;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 333;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 334;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 335;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 336;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 337;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 338;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 340;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 341;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 345;
UPDATE bank_transactions SET used = 1, manual_classification = 'OWNER_DRAW', notes = 'Branch transfer to another account | Owner draw to Dwayne (transfer)' WHERE id = 346;
UPDATE bank_transactions SET used = 1, manual_classification = 'SHAREHOLDER_LOAN', notes = 'Loan repaid by Dwayne (transfer)' WHERE id = 347;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 349;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 350;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 351;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 352;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 354;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 355;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 356;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 357;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 358;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 360;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 361;
UPDATE bank_transactions SET used = 1, manual_classification = 'SHAREHOLDER_LOAN', notes = 'Loan issued to Thomas (e-transfer)' WHERE id = 362;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 363;
UPDATE bank_transactions SET used = 1, manual_classification = 'OWNER_DRAW', notes = 'Owner draw to Thomas (e-transfer)' WHERE id = 364;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 365;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 366;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 367;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 368;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 369;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 370;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 371;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 372;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 375;
UPDATE bank_transactions SET used = 1, manual_classification = 'OWNER_DRAW', notes = 'Owner draw to Dwayne | Owner draw to Dwayne (cheque 83785012)' WHERE id = 377;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 378;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 379;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 380;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 383;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 384;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 387;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 388;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 389;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 390;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 392;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).' WHERE id = 393;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).' WHERE id = 394;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).' WHERE id = 395;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).' WHERE id = 396;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).' WHERE id = 397;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 398;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 400;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 403;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 404;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 405;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 406;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 408;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 409;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 410;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 412;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 416;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 418;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 419;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 420;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 421;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 422;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 424;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 427;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 428;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 429;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 430;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 431;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 432;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 435;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 436;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 437;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 438;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 442;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 443;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 444;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 445;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 446;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 447;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 448;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 449;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 450;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 453;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 454;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 457;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 458;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 459;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 460;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 461;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 462;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 463;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 464;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 465;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 466;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 467;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 468;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 469;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 470;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 471;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 472;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 473;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 474;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 475;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 476;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 477;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 478;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 479;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 481;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 482;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 483;
UPDATE bank_transactions SET used = 0, manual_classification = 'VENDOR_PAYMENT', notes = 'Sysco vendor payment' WHERE id = 487;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 489;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 490;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 491;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 492;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 493;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 494;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 495;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 497;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 500;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 501;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 503;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 504;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 505;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 506;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 507;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 508;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 509;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 511;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 512;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 515;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 516;
UPDATE bank_transactions SET used = 1, manual_classification = 'SHIPPING', notes = 'UPS shipping' WHERE id = 517;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 518;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 519;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 520;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 521;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 522;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 523;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 524;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 525;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 526;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Thomas payment for: Esso - Bill ' WHERE id = 527;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 528;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Walmart purchase' WHERE id = 530;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 533;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 534;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 535;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 536;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 537;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 538;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 539;
UPDATE bank_transactions SET used = 1, manual_classification = 'INTERNAL_TRANSFER', notes = 'Branch transfer to another account' WHERE id = 540;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 543;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 546;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 547;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 548;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 549;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 551;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 552;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 555;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 556;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 557;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 558;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 559;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 560;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 561;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 562;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 563;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 564;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 565;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 566;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 568;
UPDATE bank_transactions SET used = 1, manual_classification = 'UTILITIES', notes = 'Bell Aliant phone/internet' WHERE id = 569;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 571;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 572;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 573;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 574;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 575;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 576;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 577;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 578;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 579;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 580;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 581;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 582;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 583;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 585;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 588;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 591;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 592;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 593;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 594;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 595;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 596;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 597;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 598;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 601;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 604;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 605;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 606;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 607;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 608;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 609;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 610;
UPDATE bank_transactions SET used = 0, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Costco - Bill' WHERE id = 611;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 612;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 613;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 614;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 615;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 616;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 617;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 618;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 619;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 620;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 621;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 622;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 623;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 624;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 626;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Mary Butcher | Employee payroll e-transfer' WHERE id = 632;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 633;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 634;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 635;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 636;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 637;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Employee payroll e-transfer' WHERE id = 639;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 640;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 641;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 643;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 644;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 645;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 646;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 647;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 648;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 649;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 650;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 651;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 652;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 653;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 654;
UPDATE bank_transactions SET used = 1, manual_classification = 'INSURANCE', notes = 'BFL Insurance payment' WHERE id = 655;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 657;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 660;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 661;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 662;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 663;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 664;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 668;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 670;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 671;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 672;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 673;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 674;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 675;
UPDATE bank_transactions SET used = 1, manual_classification = 'OWNER_DRAW', notes = 'Owner draw to Thomas (e-transfer)' WHERE id = 676;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 677;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 678;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 679;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 680;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 681;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 682;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 683;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 684;
UPDATE bank_transactions SET used = 1, manual_classification = 'OWNER_DRAW', notes = 'Owner draw to Dwayne | Owner draw to Dwayne (cheque 72460628)' WHERE id = 688;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 689;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 690;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 691;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 692;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 696;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 697;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 698;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 699;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 700;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 702;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 703;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 705;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 708;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 709;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 711;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 712;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 713;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 714;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 715;
UPDATE bank_transactions SET used = 0, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Atlantic Superstore - Bill' WHERE id = 716;
UPDATE bank_transactions SET used = 1, manual_classification = 'STAFF_EXPENSE', notes = 'Christmas party 2024 - $200 + HST reimbursement to Dwayne' WHERE id = 717;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 718;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 724;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 725;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 726;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 727;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 728;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 729;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 730;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 731;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 732;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 733;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 734;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 735;
UPDATE bank_transactions SET used = 0, manual_classification = 'VENDOR_PAYMENT', notes = 'One-time vendor payment' WHERE id = 737;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 738;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 740;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 742;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 743;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 744;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 745;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 748;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 749;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 750;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 751;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 752;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 753;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 754;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 755;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 756;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Employee payroll e-transfer' WHERE id = 757;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 759;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 761;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Thomas payment for: Town of Amherst' WHERE id = 762;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Cost of goods sold baked goods | Lil'' Em''s vendor payment' WHERE id = 767;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Cost of goods sold baked goods | Lil'' Em''s vendor payment' WHERE id = 768;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Employee payroll e-transfer' WHERE id = 770;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 771;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 772;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 773;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 774;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 775;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 776;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 777;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 778;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 779;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 780;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Walmart - Bill' WHERE id = 781;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'One-time vendor payment' WHERE id = 782;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 783;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 784;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Dollarama - Bill' WHERE id = 785;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 786;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 787;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 789;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: GFS - Bill 9013824877' WHERE id = 790;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 791;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 792;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 793;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 794;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 796;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 797;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 798;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 801;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 802;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 803;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 807;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 808;
UPDATE bank_transactions SET used = 0, manual_classification = 'VENDOR_PAYMENT', notes = 'One-time vendor payment' WHERE id = 809;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 810;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 814;
UPDATE bank_transactions SET used = 1, manual_classification = 'EFT_PAYMENT', notes = 'EFT misc payment' WHERE id = 816;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 817;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 818;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 819;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 820;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 821;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 822;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 823;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 824;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 826;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 827;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 828;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Employee payroll e-transfer' WHERE id = 830;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 831;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 834;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 835;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 839;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 840;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 841;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 842;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 843;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 844;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Thomas payment for: Pharmasave - Bill' WHERE id = 845;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 846;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 847;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 848;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 849;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 850;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 851;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 856;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 857;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 858;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 859;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 860;
UPDATE bank_transactions SET used = 1, manual_classification = 'CRA_PAYMENT', notes = 'CRA remittance (HST or payroll)' WHERE id = 862;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 864;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 865;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 866;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 867;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 868;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 869;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 870;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 872;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 873;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 874;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 875;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 876;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 877;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 879;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 880;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 882;
UPDATE bank_transactions SET used = 1, manual_classification = 'CASH_WITHDRAWAL', notes = 'ATM/branch cash withdrawal' WHERE id = 884;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 887;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 888;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 889;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 890;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 891;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 892;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 893;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 894;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 895;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 896;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 897;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 898;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 900;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Walmart purchase' WHERE id = 902;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill' WHERE id = 903;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 904;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 905;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 906;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 909;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 910;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 911;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 912;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 913;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 914;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 915;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 916;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 917;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 918;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 920;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 921;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 922;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 923;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 924;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 925;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 926;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 927;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 928;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 929;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 931;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 933;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 935;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 936;
UPDATE bank_transactions SET used = 1, manual_classification = 'CASH_WITHDRAWAL', notes = 'ATM/branch cash withdrawal' WHERE id = 937;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 942;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 943;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 944;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 945;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 946;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 947;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 948;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 949;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 950;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 951;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 952;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: shell October 7 | Thomas payment for: Shell Gas - Bill' WHERE id = 953;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 3110269' WHERE id = 954;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 959;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 960;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 961;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 962;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 963;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: payroll September reimburse' WHERE id = 965;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 966;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 967;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 968;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 969;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 970;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 971;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 972;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 975;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 976;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 977;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 980;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 981;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 982;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 983;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 984;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 985;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 986;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 988;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 989;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 990;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 991;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Dollarama purchase' WHERE id = 992;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 993;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 994;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 995;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 996;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: reimburse for change' WHERE id = 997;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: reimburse for change' WHERE id = 998;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 1003;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1004;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1005;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1006;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 1007;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1008;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1009;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1011;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1012;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1013;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1014;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1015;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1019;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1020;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1021;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1022;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1023;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1024;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 1026;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1027;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1028;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 1029;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1031;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1034;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1036;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1038;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1039;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1040;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1041;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: August September rent' WHERE id = 1042;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kyler Edwards | Employee payroll e-transfer' WHERE id = 1043;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1044;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1045;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1048;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1049;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Kaylee Gallagher | Employee payroll e-transfer' WHERE id = 1051;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: tv for menu board | Thomas payment for: Facebook Marketplace - Bill' WHERE id = 1052;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1053;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1054;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1055;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1056;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Atlantic Superstore - Bill' WHERE id = 1057;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1058;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 30000969' WHERE id = 1059;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1060;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1061;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1062;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: canteen change' WHERE id = 1063;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: Canteen change' WHERE id = 1064;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1065;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1066;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1067;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1068;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1069;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: straws' WHERE id = 1071;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1072;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1073;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Denise Manley - reimbursement' WHERE id = 1074;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1076;
UPDATE bank_transactions SET used = 0, manual_classification = 'REIMBURSEMENT', notes = 'Email note: July rent | Reimbursement for: Town of Amherst' WHERE id = 1077;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1079;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: change reimbursement' WHERE id = 1080;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Sysco vendor payment' WHERE id = 1081;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1082;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1083;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll for Thomas' WHERE id = 1085;
UPDATE bank_transactions SET used = 1, manual_classification = 'SHAREHOLDER_LOAN', notes = 'Shareholder loan repayment - later paid as owner draw next year | Loan issued to Dwayne (cheque 72585461)' WHERE id = 1086;
UPDATE bank_transactions SET used = 1, manual_classification = 'DONATION', notes = 'Canadian Cancer Society donation' WHERE id = 1090;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1092;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1093;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1094;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1096;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1097;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1098;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1099;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1100;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1102;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1103;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1104;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1105;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1106;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: rags from bridge | Thomas payment for: Bridge Workshop - Bill' WHERE id = 1109;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: change reimburse' WHERE id = 1110;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1111;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1113;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Thomas payment for: Town of Amherst' WHERE id = 1114;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1115;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1116;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1117;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1118;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1119;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1120;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1121;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: April Payroll reimburse' WHERE id = 1122;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1123;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1124;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1125;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1127;
UPDATE bank_transactions SET used = 0, manual_classification = 'VENDOR_PAYMENT', notes = 'Price gun/stickers/clothes tagger auction win | One-time vendor payment' WHERE id = 1128;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 25' WHERE id = 1131;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1132;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1133;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1134;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1135;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1136;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1137;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1141;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1143;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1144;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1145;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1146;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1147;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: April rent | Thomas payment for: Town of Amherst - Bill april rent' WHERE id = 1148;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1149;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1151;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1152;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1153;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1154;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1155;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1156;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1157;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1158;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1163;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1164;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1165;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1166;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1167;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1168;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1169;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1171;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1173;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1174;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1175;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: reimburse March payroll' WHERE id = 1178;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1179;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1181;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'One-time vendor payment' WHERE id = 1182;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1184;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1185;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1187;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1189;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1190;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1193;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1194;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1195;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1196;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1197;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1198;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1199;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1201;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1203;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1204;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1205;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1206;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1207;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1208;
UPDATE bank_transactions SET used = 1, manual_classification = 'EFT_PAYMENT', notes = 'EFT misc payment' WHERE id = 1211;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1212;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1213;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1214;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1216;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1217;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1218;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1219;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 2425069' WHERE id = 1223;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 2437469' WHERE id = 1224;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: March rent reimbursement | Thomas payment for: Town of Amherst - Bill March Rent' WHERE id = 1225;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1228;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1229;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1230;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1231;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1232;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1233;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1234;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1235;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1236;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: February payroll reimbursement' WHERE id = 1237;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1238;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1239;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1240;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1242;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 2423469' WHERE id = 1243;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1247;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1248;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1249;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1250;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1251;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1252;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1253;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1254;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: February payroll' WHERE id = 1255;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1258;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1260;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1262;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1264;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1266;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1268;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1270;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1271;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1272;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1273;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1274;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1275;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: January payroll reimbursement' WHERE id = 1276;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1277;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1278;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1279;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1280;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1282;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 2365969' WHERE id = 1284;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1285;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: Bembridges bootleg sauces Inc. reimbursement | Thomas payment for: Jeff Bembridge - Bill' WHERE id = 1286;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Electric Kitty - Bill' WHERE id = 1287;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1288;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1289;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1290;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1291;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1292;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1293;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1294;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1295;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1296;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1297;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1298;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1299;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1300;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1301;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1302;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1307;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1309;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1314;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1315;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1316;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1317;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1318;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1320;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1322;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note match invoice Jan 14 oil damaged reimbursement. gfs 9005546522 (ref C1AWgjhaHcje) | Email note: Jan 14 oil damaged reimbursement. gfs 9005546522 | Reimbursement for: GFS - Bill 9005546522' WHERE id = 1323;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: 10 oil 20 each weds Feb 7 gfs | Thomas payment for: GFS - Bill' WHERE id = 1324;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1325;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1326;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1329;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1331;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1333;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1334;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1335;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1336;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1337;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1339;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1341;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1343;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1344;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1345;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1346;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1347;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1348;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1349;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 1350;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Email note: February rent reimbursement | Thomas payment for: Town of Amherst - Bill FEbruary REnt' WHERE id = 1351;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1352;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1353;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1357;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1362;
UPDATE bank_transactions SET used = 1, manual_classification = 'INSURANCE', notes = 'BFL Insurance payment' WHERE id = 1363;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Tyson Ogden | Employee payroll e-transfer' WHERE id = 1364;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: canteen q3/q4 payroll remittance reimbursement' WHERE id = 1365;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1366;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1367;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1368;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1369;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1370;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1371;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1372;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1374;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1378;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1379;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1380;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 1382;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1384;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1387;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1388;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note: cheese curds from GFS reimbursement | Reimbursement for: GFS - Bill 9005534423' WHERE id = 1390;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1391;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1393;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1394;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1395;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill 2220169' WHERE id = 1396;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1398;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1399;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1401;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1402;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1403;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1404;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 1405;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: Corp paid for Keg' WHERE id = 1408;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1409;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1410;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1411;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1412;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1413;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1414;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1415;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1416;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1418;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1419;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1420;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1421;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1422;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note: pharmasave dec9th | Reimbursement for: Pharmasave - Bill' WHERE id = 1423;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1424;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1425;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1426;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1428;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1430;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1431;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1433;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1437;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1438;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1441;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1444;
UPDATE bank_transactions SET used = 1, manual_classification = 'DONATION', notes = 'Sponsorship: kid''s hockey team/jersey (Tim Rich)' WHERE id = 1446;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Daniel Gionet - Mondoux vendor' WHERE id = 1447;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1448;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1449;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1450;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1451;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1452;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1454;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1455;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1458;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1459;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1460;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1461;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1465;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1466;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1468;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1469;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'BMO Mastercard payment' WHERE id = 1470;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1471;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1472;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1473;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1474;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1475;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1476;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1477;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note: December rent | Reimbursement for: Town of Amherst - Bill' WHERE id = 1478;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1481;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1482;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1483;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1485;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to MADDISON TROOP | Maddison Troop - employee' WHERE id = 1487;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1488;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1489;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1491;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Town of Amherst - Bill' WHERE id = 1492;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1494;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1498;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1500;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = 'Email note: curlys invoice 1994069 | Invoice 1994069 inserted from PDF; missed in HST filings FY2024' WHERE id = 1503;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1504;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1506;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: curlys change over to canteen change' WHERE id = 1508;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Anthony MacDonald | Employee payroll e-transfer' WHERE id = 1509;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to MADDISON TROOP | Maddison Troop - employee' WHERE id = 1510;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1511;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1513;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1516;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1517;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1518;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1519;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1520;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Curly''s Sports and Supplements - Bill D1' WHERE id = 1521;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1524;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1525;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1526;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1528;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1529;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1530;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1533;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1534;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1535;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = 'Email note: dollarama Oct 28' WHERE id = 1536;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1537;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1538;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1539;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1540;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Snaxies vendor payment' WHERE id = 1542;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1543;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1546;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1547;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1548;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1549;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1550;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1551;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1553;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1554;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1557;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1558;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Mondoux - Bill 8100383' WHERE id = 1559;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1560;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1563;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1564;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1565;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1566;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1568;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1569;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1570;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1571;
UPDATE bank_transactions SET used = 0, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Atlantic Superstore - Bill' WHERE id = 1572;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1573;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1574;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1575;
UPDATE bank_transactions SET used = 0, manual_classification = NULL, notes = NULL WHERE id = 1576;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1577;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1578;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1579;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1580;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1581;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1582;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1583;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1584;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1585;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1586;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1587;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1588;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1589;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1590;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1591;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1592;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1593;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1594;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1595;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1596;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1597;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1598;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1600;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1601;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1602;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1603;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1604;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1605;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1606;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1607;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'CIBC Visa payment' WHERE id = 1608;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1612;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1614;
UPDATE bank_transactions SET used = 0, manual_classification = 'REIMBURSEMENT', notes = 'Email note: October rent | Reimbursement for: Town of Amherst - Bill' WHERE id = 1615;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = 'Email note: curds reimbursement' WHERE id = 1617;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note: june 7th ns food permit | Reimbursement for: Gov''t of Nova Scotia - Bill 5932' WHERE id = 1618;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 1620;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1622;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1623;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1627;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1629;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1630;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1631;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1632;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1633;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1634;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1637;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1638;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note: June full rent 700 + hst | Reimbursement for: Town of Amherst' WHERE id = 1639;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: Amazon - Bill ' WHERE id = 1640;
UPDATE bank_transactions SET used = 1, manual_classification = NULL, notes = NULL WHERE id = 1641;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1642;
UPDATE bank_transactions SET used = 1, manual_classification = 'CC_PAYMENT', notes = 'Payment to CIBC credit card' WHERE id = 1643;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Daniel Gionet - Mondoux vendor' WHERE id = 1645;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1647;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Walmart purchase' WHERE id = 1648;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Dollarama purchase' WHERE id = 1649;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1651;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAYMENT', notes = 'Covered Bridge Chips vendor' WHERE id = 1656;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Email note match invoice GFS 9002908697 Aug 11 (ref C1AkVXdW3xAW) | Email note: GFS 9002908697 Aug 11 | Reimbursement for: GFS - Bill 9002908697' WHERE id = 1658;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: GFS - Bill 9002912093' WHERE id = 1659;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: GFS - Bill 9002186430' WHERE id = 1660;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: GFS - Bill 9002189920' WHERE id = 1661;
UPDATE bank_transactions SET used = 1, manual_classification = 'REIMBURSEMENT', notes = 'Reimbursement for: GFS - Bill 9002081541' WHERE id = 1662;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1663;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PAD', notes = 'GFS/Capital Foods PAD payment' WHERE id = 1665;
UPDATE bank_transactions SET used = 1, manual_classification = 'PAYROLL_ETRANSFER', notes = 'Payroll e-transfer to Jesse Goodwin | Employee payroll e-transfer' WHERE id = 1669;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 1672;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1676;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1677;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Walmart purchase' WHERE id = 1679;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Dollarama purchase' WHERE id = 1680;
UPDATE bank_transactions SET used = 1, manual_classification = 'RENT', notes = 'Town of Amherst rent' WHERE id = 1681;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1683;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1684;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1685;
UPDATE bank_transactions SET used = 1, manual_classification = 'VENDOR_PURCHASE', notes = 'Walmart purchase' WHERE id = 1686;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1688;
UPDATE bank_transactions SET used = 1, manual_classification = 'INTERNAL_TRANSFER', notes = 'Branch transfer to another account' WHERE id = 1689;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1690;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1691;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1692;
UPDATE bank_transactions SET used = 1, manual_classification = 'BANK_FEE', notes = 'CIBC account fee' WHERE id = 1693;
-- Credit card transaction flags (used/funded_by_bank_txn_id)
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 35 WHERE id = 23;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 36 WHERE id = 24;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 34 WHERE id = 25;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 30 WHERE id = 26;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 29 WHERE id = 27;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 31 WHERE id = 28;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 70 WHERE id = 48;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 65 WHERE id = 49;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 64 WHERE id = 50;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 67 WHERE id = 51;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 66 WHERE id = 52;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 98 WHERE id = 70;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 96 WHERE id = 71;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 95 WHERE id = 72;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 97 WHERE id = 73;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 93 WHERE id = 74;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 92 WHERE id = 75;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 91 WHERE id = 76;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 112 WHERE id = 95;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 121 WHERE id = 97;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 123 WHERE id = 98;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 120 WHERE id = 99;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 122 WHERE id = 105;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 133 WHERE id = 116;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 134 WHERE id = 117;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 135 WHERE id = 118;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 140 WHERE id = 119;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 139 WHERE id = 120;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 138 WHERE id = 121;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 137 WHERE id = 122;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 148 WHERE id = 123;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 147 WHERE id = 124;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 146 WHERE id = 125;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 145 WHERE id = 126;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 144 WHERE id = 127;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 143 WHERE id = 128;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 151 WHERE id = 129;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 149 WHERE id = 130;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 157 WHERE id = 131;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 154 WHERE id = 132;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 155 WHERE id = 133;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 141 WHERE id = 134;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 198 WHERE id = 174;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 206 WHERE id = 177;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 207 WHERE id = 179;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 217 WHERE id = 187;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 216 WHERE id = 188;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 223 WHERE id = 193;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 264 WHERE id = 225;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 265 WHERE id = 228;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 283 WHERE id = 259;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 286 WHERE id = 271;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 292 WHERE id = 300;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 311 WHERE id = 323;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 308 WHERE id = 324;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 322 WHERE id = 326;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 318 WHERE id = 327;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 319 WHERE id = 328;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 317 WHERE id = 330;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 321 WHERE id = 331;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 348;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 335 WHERE id = 360;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 336 WHERE id = 361;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 334 WHERE id = 362;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 375;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 381;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 350 WHERE id = 384;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 387;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 354 WHERE id = 389;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 355 WHERE id = 390;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 356 WHERE id = 391;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 357 WHERE id = 393;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 400;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 372 WHERE id = 402;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 368 WHERE id = 403;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 366 WHERE id = 404;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 369 WHERE id = 405;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 371 WHERE id = 406;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 408;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 409;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 416;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 395 WHERE id = 421;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 393 WHERE id = 422;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 394 WHERE id = 423;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 396 WHERE id = 426;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 397 WHERE id = 427;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 433;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 404 WHERE id = 434;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 406 WHERE id = 435;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 440;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 429 WHERE id = 449;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 430 WHERE id = 450;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 431 WHERE id = 451;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 428 WHERE id = 453;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 456;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 457;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 460;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 461;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 462;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 463;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 442 WHERE id = 464;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 449 WHERE id = 465;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 450 WHERE id = 466;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 467;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 468;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 444 WHERE id = 469;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 443 WHERE id = 470;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 447 WHERE id = 471;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 446 WHERE id = 472;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 474;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 478;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 453 WHERE id = 479;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 454 WHERE id = 480;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 481;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 482;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 466 WHERE id = 485;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 464 WHERE id = 486;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 475 WHERE id = 487;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 461 WHERE id = 489;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 460 WHERE id = 490;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 459 WHERE id = 491;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 462 WHERE id = 492;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 469 WHERE id = 493;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 472 WHERE id = 494;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 471 WHERE id = 495;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 470 WHERE id = 496;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 500;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 501;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 503;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 512;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 513;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 515;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 516;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 501 WHERE id = 521;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 520 WHERE id = 528;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 516 WHERE id = 529;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 523 WHERE id = 533;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 524 WHERE id = 534;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 525 WHERE id = 535;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 526 WHERE id = 536;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 528 WHERE id = 537;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 539;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 551;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 556;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 564;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 566;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 567;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 569;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 570;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 555 WHERE id = 572;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 556 WHERE id = 573;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 559 WHERE id = 574;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 560 WHERE id = 575;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 562 WHERE id = 576;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 577 WHERE id = 588;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 578 WHERE id = 589;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 576 WHERE id = 590;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 592;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 593;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 594;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 598;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 604;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 607;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 623;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 632;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 614 WHERE id = 634;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 616 WHERE id = 635;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 615 WHERE id = 636;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 618 WHERE id = 637;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 617 WHERE id = 638;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 613 WHERE id = 639;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 641;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 643;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 645;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 647;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 656;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 646 WHERE id = 660;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 654 WHERE id = 661;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 644 WHERE id = 662;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 664;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 665;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 668;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 679 WHERE id = 676;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 683;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 740 WHERE id = 705;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 707;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 786 WHERE id = 716;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 779 WHERE id = 717;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 728;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 732;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 823 WHERE id = 736;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 841 WHERE id = 743;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 755;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 858 WHERE id = 762;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 866 WHERE id = 768;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 865 WHERE id = 769;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 873 WHERE id = 771;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 775;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 889 WHERE id = 778;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 779;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 781;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 808;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 952 WHERE id = 810;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 813;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1023 WHERE id = 843;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 856;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1054 WHERE id = 864;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 872;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 879;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1067 WHERE id = 885;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1066 WHERE id = 886;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1072 WHERE id = 903;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1073 WHERE id = 905;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 913;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 916;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1079 WHERE id = 957;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 962;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1093 WHERE id = 1022;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1094 WHERE id = 1023;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1024;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1025;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1096 WHERE id = 1032;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1097 WHERE id = 1035;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1036;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1102 WHERE id = 1048;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1103 WHERE id = 1049;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1104 WHERE id = 1050;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1059;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1115 WHERE id = 1085;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1086;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1120 WHERE id = 1087;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1119 WHERE id = 1088;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1118 WHERE id = 1089;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1093;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1094;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1095;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1124 WHERE id = 1100;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1114;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1127 WHERE id = 1118;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1135 WHERE id = 1119;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1136 WHERE id = 1120;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1137 WHERE id = 1121;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1123;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1124;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1125;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1145 WHERE id = 1131;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1144 WHERE id = 1132;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1147 WHERE id = 1133;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1146 WHERE id = 1134;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1140;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1141;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1143;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1144;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1194 WHERE id = 1167;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1193 WHERE id = 1168;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1170;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1174;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1179;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1208 WHERE id = 1180;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1207 WHERE id = 1181;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1205 WHERE id = 1182;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1206 WHERE id = 1183;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1204 WHERE id = 1184;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1187;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1188;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1189;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1190;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1235 WHERE id = 1203;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1205;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1252 WHERE id = 1209;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1249 WHERE id = 1210;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1250 WHERE id = 1211;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1214;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1218;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1219;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1275 WHERE id = 1229;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1274 WHERE id = 1230;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1271 WHERE id = 1231;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1270 WHERE id = 1232;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1235;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1239;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1240;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1302 WHERE id = 1244;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1289 WHERE id = 1245;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1288 WHERE id = 1246;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1293 WHERE id = 1247;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1295 WHERE id = 1248;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1299 WHERE id = 1249;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1298 WHERE id = 1250;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1300 WHERE id = 1251;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1256;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1258;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1259;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1264;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1267;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1268;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1274;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1277;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1280;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1283;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1325 WHERE id = 1290;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1326 WHERE id = 1291;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1292;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1295;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1333 WHERE id = 1296;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1337 WHERE id = 1297;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1336 WHERE id = 1299;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1348 WHERE id = 1302;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1346 WHERE id = 1303;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1349 WHERE id = 1304;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1343 WHERE id = 1305;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1345 WHERE id = 1306;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1344 WHERE id = 1307;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1310;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1311;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1312;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1316;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1317;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1322;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1325;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1372 WHERE id = 1330;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1370 WHERE id = 1331;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1371 WHERE id = 1332;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1368 WHERE id = 1333;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1369 WHERE id = 1334;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1336;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1337;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1340;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1343;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1344;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1387 WHERE id = 1348;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1388 WHERE id = 1349;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1391 WHERE id = 1350;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1393 WHERE id = 1352;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1398 WHERE id = 1353;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1356;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1358;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1360;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1362;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1402 WHERE id = 1365;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1404 WHERE id = 1366;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1411 WHERE id = 1369;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1410 WHERE id = 1370;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1409 WHERE id = 1371;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1412 WHERE id = 1372;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1416 WHERE id = 1373;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1415 WHERE id = 1374;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1414 WHERE id = 1375;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1422 WHERE id = 1385;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1424 WHERE id = 1386;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1421 WHERE id = 1387;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1426 WHERE id = 1388;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1455 WHERE id = 1410;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1459 WHERE id = 1413;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1416;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1474 WHERE id = 1417;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1473 WHERE id = 1418;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1472 WHERE id = 1419;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1475 WHERE id = 1421;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1489 WHERE id = 1434;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1436;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1458;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1517 WHERE id = 1464;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1518 WHERE id = 1466;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1519 WHERE id = 1468;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1471;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1481;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1529 WHERE id = 1483;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1484;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1485;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1530 WHERE id = 1486;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1533 WHERE id = 1489;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1535 WHERE id = 1490;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1534 WHERE id = 1491;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1538 WHERE id = 1497;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1540 WHERE id = 1498;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1505;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1550 WHERE id = 1506;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1549 WHERE id = 1507;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1547 WHERE id = 1509;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1554 WHERE id = 1513;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1558 WHERE id = 1518;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1557 WHERE id = 1519;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1523;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1524;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1571 WHERE id = 1532;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1570 WHERE id = 1533;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1581 WHERE id = 1534;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1578 WHERE id = 1535;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1577 WHERE id = 1536;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1579 WHERE id = 1537;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1589 WHERE id = 1538;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1590 WHERE id = 1539;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1584 WHERE id = 1540;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1585 WHERE id = 1541;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1587 WHERE id = 1542;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1586 WHERE id = 1543;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1592 WHERE id = 1544;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1593 WHERE id = 1545;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1594 WHERE id = 1546;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1598 WHERE id = 1547;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1604 WHERE id = 1551;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1608 WHERE id = 1552;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1553;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1581;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1583;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1619;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1624;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1626;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1628;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1631;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1644;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1645;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1646;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1657;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1658;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1663;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1665;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1671;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1727;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1728;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1730;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1734;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1737;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1764;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1793;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1806;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1846;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1859;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 1865;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 32 WHERE id = 2239;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 33 WHERE id = 2241;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 68 WHERE id = 2291;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 126 WHERE id = 2373;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 127 WHERE id = 2374;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 156 WHERE id = 2384;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 185 WHERE id = 2421;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 197 WHERE id = 2438;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 196 WHERE id = 2439;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 202 WHERE id = 2448;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 242 WHERE id = 2498;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 243 WHERE id = 2499;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 246 WHERE id = 2502;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 262 WHERE id = 2522;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 263 WHERE id = 2523;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 268 WHERE id = 2524;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 307 WHERE id = 2736;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 313 WHERE id = 2748;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 320 WHERE id = 2751;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 337 WHERE id = 2796;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 448 WHERE id = 2980;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 2983;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 468 WHERE id = 2987;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3003;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 519 WHERE id = 3032;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3034;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3040;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3060;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 565 WHERE id = 3062;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 564 WHERE id = 3063;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 558 WHERE id = 3064;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 557 WHERE id = 3065;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3066;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3085;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3086;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3087;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 612 WHERE id = 3106;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 608 WHERE id = 3107;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 610 WHERE id = 3108;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 609 WHERE id = 3109;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 605 WHERE id = 3110;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 606 WHERE id = 3111;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3112;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3124;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3125;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3127;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3128;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3130;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 645 WHERE id = 3135;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 652 WHERE id = 3136;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 650 WHERE id = 3137;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 648 WHERE id = 3138;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 649 WHERE id = 3139;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 647 WHERE id = 3140;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 653 WHERE id = 3141;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3150;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3151;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3152;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3153;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3154;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3158;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3159;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 681 WHERE id = 3161;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 680 WHERE id = 3162;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 678 WHERE id = 3163;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 677 WHERE id = 3164;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3172;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3173;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3174;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3176;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3182;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 699 WHERE id = 3183;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 698 WHERE id = 3184;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 714 WHERE id = 3210;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 713 WHERE id = 3211;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3218;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 726 WHERE id = 3225;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 729 WHERE id = 3226;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3237;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3248;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3251;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 744 WHERE id = 3255;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 745 WHERE id = 3256;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 756 WHERE id = 3261;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 753 WHERE id = 3262;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 754 WHERE id = 3263;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3275;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3279;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3280;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3290;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 783 WHERE id = 3293;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 784 WHERE id = 3294;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 780 WHERE id = 3295;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 771 WHERE id = 3296;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 778 WHERE id = 3297;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 775 WHERE id = 3298;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 774 WHERE id = 3299;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 773 WHERE id = 3300;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3306;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3309;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3320;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3321;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3323;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3327;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3330;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 821 WHERE id = 3333;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 824 WHERE id = 3336;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 822 WHERE id = 3337;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3341;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3347;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3349;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 839 WHERE id = 3350;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 844 WHERE id = 3352;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 846 WHERE id = 3353;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 842 WHERE id = 3354;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3355;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3356;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3357;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3361;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 874 WHERE id = 3365;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 872 WHERE id = 3366;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3369;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3374;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 887 WHERE id = 3377;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 891 WHERE id = 3378;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 892 WHERE id = 3379;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3382;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3384;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 906 WHERE id = 3386;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3387;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3391;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 918 WHERE id = 3392;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 924 WHERE id = 3394;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 921 WHERE id = 3395;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 920 WHERE id = 3396;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3399;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3402;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3407;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 945 WHERE id = 3408;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 951 WHERE id = 3414;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3415;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3417;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 971 WHERE id = 3424;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 966 WHERE id = 3426;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 967 WHERE id = 3427;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 968 WHERE id = 3428;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3430;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3432;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3434;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3439;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 975 WHERE id = 3442;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 982 WHERE id = 3451;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 980 WHERE id = 3452;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 985 WHERE id = 3453;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 986 WHERE id = 3454;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3458;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 995 WHERE id = 3465;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 996 WHERE id = 3466;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3467;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3470;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3471;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3473;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1009 WHERE id = 3474;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3475;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3477;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1021 WHERE id = 3479;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1020 WHERE id = 3480;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1022 WHERE id = 3481;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1024 WHERE id = 3482;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3485;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3486;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1040 WHERE id = 3502;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1039 WHERE id = 3503;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3505;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3506;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3507;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3510;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1049 WHERE id = 3513;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3515;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1053 WHERE id = 3517;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1056 WHERE id = 3518;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3519;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3524;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3533;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1068 WHERE id = 3547;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3551;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1098 WHERE id = 3673;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1111 WHERE id = 3692;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3695;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1117 WHERE id = 3697;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1116 WHERE id = 3699;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1156 WHERE id = 3733;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1155 WHERE id = 3734;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1158 WHERE id = 3737;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1157 WHERE id = 3738;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3742;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3744;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3749;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3751;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1169 WHERE id = 3752;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1168 WHERE id = 3753;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1167 WHERE id = 3754;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3755;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3756;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3757;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1175 WHERE id = 3758;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1174 WHERE id = 3760;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3761;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1195 WHERE id = 3775;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3782;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1219 WHERE id = 3796;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3797;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1216 WHERE id = 3800;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1217 WHERE id = 3801;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3802;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3805;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1236 WHERE id = 3806;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3808;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1254 WHERE id = 3810;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3814;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3829;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1268 WHERE id = 3833;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1272 WHERE id = 3838;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3839;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1292 WHERE id = 3844;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3852;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1318 WHERE id = 3859;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3863;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3868;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1335 WHERE id = 3870;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1334 WHERE id = 3871;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3874;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1341 WHERE id = 3877;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1347 WHERE id = 3879;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3887;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3898;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3899;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1379 WHERE id = 3902;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1378 WHERE id = 3903;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1394 WHERE id = 3913;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1395 WHERE id = 3914;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1399 WHERE id = 3917;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3919;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1403 WHERE id = 3920;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1401 WHERE id = 3921;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3922;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1413 WHERE id = 3931;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1437 WHERE id = 3953;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3973;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1460 WHERE id = 3980;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1458 WHERE id = 3981;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3985;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1466 WHERE id = 3989;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 3992;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1476 WHERE id = 3997;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1471 WHERE id = 3998;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1469 WHERE id = 3999;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4000;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1483 WHERE id = 4001;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1482 WHERE id = 4002;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4004;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1494 WHERE id = 4022;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4033;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1506 WHERE id = 4037;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4047;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1520 WHERE id = 4048;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1516 WHERE id = 4049;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4051;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4052;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4053;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1537 WHERE id = 4054;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1539 WHERE id = 4055;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1551 WHERE id = 4056;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1548 WHERE id = 4057;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4058;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1560 WHERE id = 4063;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1563 WHERE id = 4065;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1564 WHERE id = 4066;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1565 WHERE id = 4067;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1597 WHERE id = 4069;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1582 WHERE id = 4070;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1583 WHERE id = 4071;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1588 WHERE id = 4072;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1595 WHERE id = 4073;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1591 WHERE id = 4074;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1596 WHERE id = 4075;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1575 WHERE id = 4076;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1573 WHERE id = 4077;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1574 WHERE id = 4078;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1580 WHERE id = 4079;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4080;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4081;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4082;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1605 WHERE id = 4083;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1607 WHERE id = 4084;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1606 WHERE id = 4085;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1601 WHERE id = 4086;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1602 WHERE id = 4087;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1603 WHERE id = 4088;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4093;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4094;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4095;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4096;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4098;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4100;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4101;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1637 WHERE id = 4116;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1638 WHERE id = 4117;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1642 WHERE id = 4118;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = 1643 WHERE id = 4119;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4121;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4123;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4131;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4132;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4133;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4135;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4143;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4144;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4149;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4152;
UPDATE cc_transactions SET used = 1, funded_by_bank_txn_id = NULL WHERE id = 4153;
COMMIT;

-- GFS 9005546522 reimbursed to Dwayne via Feb 7 e-transfer
INSERT INTO wave_matches (wave_bill_id, match_type, bank_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes) VALUES (166, 'SHAREHOLDER_REIMBURSE', 1323, 'HIGH', 'USER_MANUAL', 24, 0, 'GFS 9005546522 - Dwayne paid, reimbursed via Feb 7 e-transfer');
UPDATE bank_transactions SET used = 1, notes = 'Matched to GFS bill 9005546522 (wave_bill 166)' WHERE id = 1323;

-- Wave row 159: Dollarama $312.40 - Split payment via bank transfers
-- Bank txns 1402 ($292.30) + 1404 ($20.10) = $312.40 to card 0318
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes) VALUES (158, 'BANK_SPLIT', 1402, 29230, 'Split payment part 1');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes) VALUES (158, 'BANK_SPLIT', 1404, 2010, 'Split payment part 2');
UPDATE bank_transactions SET used = 1, notes = 'Dollarama split payment part 1 (wave_bill 158)' WHERE id = 1402;
UPDATE bank_transactions SET used = 1, notes = 'Dollarama split payment part 2 (wave_bill 158)' WHERE id = 1404;

-- Wave row 191: Esso $40.01 - User corrected CC purchase match
-- Deleted incorrect match to CC txn 3868 (Feb 5 2024), replaced with CC txn 3213 (Dec 23 2024 PROXI)
-- Bank txn 1334 (Feb 1 2024 $40.01) is the payment to card 8154
DELETE FROM wave_matches WHERE wave_bill_id = 190 AND cc_txn_id = 3868;
INSERT INTO wave_matches (wave_bill_id, match_type, cc_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
VALUES (190, 'CC_PURCHASE', 3213, 'HIGH', 'USER_MANUAL', 0, 0, 'User corrected - Dec 23 PROXI was the gas purchase');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (190, 'BANK_CC_CHAIN', 1334, 4001, 'Bank payment to card 8154 for Esso');
UPDATE bank_transactions SET used = 1, notes = 'Payment to card 8154 for Esso bill (wave_bill 190)' WHERE id = 1334;

-- Wave row 202: Gov't of Nova Scotia $61.05 - Cash reimbursed to Dwayne
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (201, 'DWAYNE', 6105, 'Card 0318; cash reimbursed to Dwayne');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (201, 'CASH_REIMBURSE', NULL, 6105, 'Cash reimbursed to Dwayne');

-- Wave row 233: We Like Work $307.50 - Paid with cash from till
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (232, 'TILL', 30750, 'Paid with cash from till');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (232, 'CASH_REIMBURSE', NULL, 30750, 'Paid with cash');

-- Wave row 295: Atlantic Superstore $152.60 - Cash reimbursed to Dwayne (paid CIBC visa Apr 16)
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (294, 'DWAYNE', 15260, 'Paid CIBC visa Apr 16; cash reimbursed to Dwayne');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (294, 'CASH_REIMBURSE', NULL, 15260, 'Cash reimbursed to Dwayne');

-- Wave row 301: Canadian Tire $41.37 - Cash reimbursed to Dwayne
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (300, 'DWAYNE', 4137, 'Card 0318; cash reimbursed to Dwayne');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (300, 'CASH_REIMBURSE', NULL, 4137, 'Cash reimbursed to Dwayne');

-- Wave row 303: Gov't of Nova Scotia $222.59 - Bank payment to card 0318 on Apr 23
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (302, 'BANK_CC_CHAIN', 1127, 22259, 'Bank payment to card 0318');
UPDATE bank_transactions SET used = 1, notes = 'Payment to card 0318 for Gov''t of NS (wave_bill 302)' WHERE id = 1127;

-- Wave row 666: Sobeys $116.58 - Bank payment to card 0318 on Mar 20
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (665, 'BANK_CC_CHAIN', 447, 11658, 'Bank payment to card 0318');
UPDATE bank_transactions SET used = 1, notes = 'Payment to card 0318 for Sobeys (wave_bill 665)' WHERE id = 447;

-- Wave row 670: Pharmasave $81.80 - Cash reimbursed to Dwayne
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (669, 'DWAYNE', 8180, 'Card 0318; cash reimbursed to Dwayne');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (669, 'CASH_REIMBURSE', NULL, 8180, 'Cash reimbursed to Dwayne');

-- Wave row 168: Pharmasave $7.38 - Complete CC chain, just needed bank txn marked
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (167, 'BANK_CC_CHAIN', 1372, 738, 'Bank payment to card 0318');
UPDATE bank_transactions SET used = 1, notes = 'Payment to card 0318 for Pharmasave (wave_bill 167)' WHERE id = 1372;

-- Wave row 706: Bell $131.53 - Paid in advance on Apr 11 to card 0318
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (705, 'BANK_CC_CHAIN', 395, 13153, 'Bell paid in advance Apr 11 to card 0318');
UPDATE bank_transactions SET used = 1, notes = 'Bell paid in advance (wave_bill 705)' WHERE id = 395;

-- Wave row 677: CIBC Q1 Account Fees - Corrected from $135 to $195 and matched to 3 bank fees
UPDATE wave_bills SET total_cents = 19500, net_cents = 19500 WHERE id = 676;
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes) VALUES (676, 'BANK_DIRECT', 596, 6500, 'Jan 31 ACCOUNT FEE');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes) VALUES (676, 'BANK_DIRECT', 511, 6500, 'Feb 28 ACCOUNT FEE');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes) VALUES (676, 'BANK_DIRECT', 418, 6500, 'Mar 31 ACCOUNT FEE');
UPDATE bank_transactions SET used = 1, notes = 'Q1 2025 Account Fee (wave_bill 676)' WHERE id IN (596, 511, 418);

-- Wave row 679: CIBC $6.00 - GPFS Service Charge Apr 1
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (678, 'BANK_DIRECT', 416, 600, 'GPFS Service Charge');
UPDATE bank_transactions SET used = 1, notes = 'CIBC GPFS Service Charge (wave_bill 678)' WHERE id = 416;

-- Wave row 698: CIBC $4.00 - GPFS Service Charge May 1
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (697, 'BANK_DIRECT', 360, 400, 'GPFS Service Charge');
UPDATE bank_transactions SET used = 1, notes = 'CIBC GPFS Service Charge (wave_bill 697)' WHERE id = 360;

-- Wave row 699: CIBC $164.78 - Cheque Order May 5 (1 cent diff: bank $164.77)
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (698, 'BANK_DIRECT', 353, 16477, 'DELUXE-CHQ ORDER (1 cent diff)');
UPDATE bank_transactions SET used = 1, notes = 'CIBC Cheque Order (wave_bill 698)' WHERE id = 353;

-- Wave row 511: Capital Foods 2596503 $148.73 - Missing credit memo 2597723 $48.12
-- Net payment: $148.73 - $48.12 = $100.61 paid Dec 18
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (510, 'BANK_DIRECT', 721, 10061, 'Paid $100.61 after $48.12 credit memo 2597723');
UPDATE bank_transactions SET used = 1, notes = 'Capital Foods 2596503 net of credit memo (wave_bill 510)' WHERE id = 721;

-- Wave row 281: Costco - Corrected from $812.89 to $811.89, paid to MC Apr 4
UPDATE wave_bills SET total_cents = 81189, net_cents = 81189 WHERE id = 280;
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (280, 'BANK_CC_CHAIN', 1174, 81189, 'Payment to MC Apr 4');
UPDATE bank_transactions SET used = 1, notes = 'Costco payment to MC (wave_bill 280)' WHERE id = 1174;
INSERT INTO wave_matches (wave_bill_id, match_type, cc_txn_id, bank_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
VALUES (280, 'CC_PURCHASE', 3762, 1174, 'HIGH', 'USER_MANUAL', 1, 0, 'Costco on card 7022, paid via bank txn to MC');
UPDATE cc_transactions SET used = 1 WHERE id = 3762;

-- Wave rows 694, 707: Nayax vending machine monthly fees - deducted from revenue (no bank txn)
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (693, 'REVENUE_DEDUCTION', NULL, 1704, 'Nayax vending machine monthly fee - deducted from revenue');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (706, 'REVENUE_DEDUCTION', NULL, 1704, 'Nayax vending machine monthly fee - deducted from revenue');

-- Wave row 686: Shopify monthly addon $49.02 -> CC txn 419 (34.18 USD)
INSERT INTO wave_matches (wave_bill_id, match_type, cc_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
VALUES (685, 'CC_PURCHASE', 419, 'HIGH', 'USER_MANUAL', 1, 1, 'Shopify monthly addon 34.18 USD');
UPDATE cc_transactions SET used = 1 WHERE id = 419;

-- Wave row 544: Shopify $412.83 - Amalgamated subscription charges paid to Visa Mar 5
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (543, 'BANK_CC_CHAIN', 501, 41283, 'Amalgamated Shopify subscription charges - paid to Visa Mar 5');
UPDATE bank_transactions SET used = 1, notes = 'Shopify amalgamated charges (wave_bill 543)' WHERE id = 501;

-- Wave row 542: Shopify 2024 CC Fees $2208.04 - Deducted from payouts
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (541, 'REVENUE_DEDUCTION', NULL, 220804, 'Shopify 2024 CC fees - deducted from payouts');

-- Wave row 686: CORRECTION - Changed from CC match to cash reimbursement to Dwayne
DELETE FROM wave_matches WHERE wave_bill_id = 685 AND cc_txn_id = 419;
UPDATE cc_transactions SET used = 0 WHERE id = 419;
INSERT INTO cash_reimbursements (wave_bill_id, reimbursed_to, amount_cents, notes)
VALUES (685, 'DWAYNE', 4902, 'Shopify monthly addon; cash reimbursed to Dwayne');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (685, 'CASH_REIMBURSE', NULL, 4902, 'Cash reimbursed to Dwayne');

-- Bank txn 1128: E-transfer to Charlie $30 - Facebook marketplace merchandising
UPDATE bank_transactions SET used = 1, manual_classification = 'BUSINESS_EXPENSE', notes = 'Facebook marketplace purchase for merchandising items' WHERE id = 1128;

-- Bank txn 1128: Create wave bill for FB Marketplace merchandising purchase
-- Note: wave_bill_id will be assigned dynamically, use invoice_number lookup
-- INSERT INTO wave_bills handled by wave_bill_overrides.csv with invoice FB-MERCH-001

-- Bank txn 1182: E-transfer to Markie B $1311 - Markis Bus Tours (wave_bill 277)
INSERT INTO wave_matches (wave_bill_id, match_type, bank_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
VALUES (277, 'E_TRANSFER', 1182, 'HIGH', 'USER_MANUAL', 1, 0, 'E-transfer to Markie B for bus tour');
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
VALUES (277, 'BANK_DIRECT', 1182, 131100, 'E-transfer to Markie B');
UPDATE bank_transactions SET used = 1, notes = 'Markis Bus Tours (wave_bill 277)' WHERE id = 1182;

-- Bank txn 527: Fix wrong PAYROLL_ETRANSFER classification - this is Thomas reimbursement for Esso bill
UPDATE bank_transactions SET manual_classification = NULL, notes = NULL WHERE id = 527;
INSERT OR IGNORE INTO wave_matches (wave_bill_id, bank_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (612, 527, 'E_TRANSFER_REIMBURSE', 'HIGH', 'manual', 1, 'Thomas reimbursed for Esso bill via e-transfer');
UPDATE bank_txn_classifications SET txn_category = 'REIMBURSEMENT', explanation = 'Reimbursement to Thomas for Esso bill (row 613)', verified = 1 WHERE bank_txn_id = 527;

-- Bank txn 591: GPFS service charge - create wave bill and link
INSERT OR IGNORE INTO wave_bills (invoice_date, vendor_raw, vendor_category, total_cents, tax_cents, net_cents)
SELECT '2025-02-03', 'CIBC - Bill GPFS Service Charge', 'BANK_FEE', 200, 0, 200
WHERE NOT EXISTS (SELECT 1 FROM wave_bills WHERE invoice_date = '2025-02-03' AND vendor_raw = 'CIBC - Bill GPFS Service Charge');
INSERT OR IGNORE INTO wave_matches (wave_bill_id, bank_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
SELECT wb.id, 591, 'BANK_DEBIT', 'EXACT', 'manual', 0, 'GPFS service charge'
FROM wave_bills wb WHERE wb.invoice_date = '2025-02-03' AND wb.vendor_raw = 'CIBC - Bill GPFS Service Charge';
UPDATE bank_txn_classifications SET txn_category = 'BANK_FEE', explanation = 'CIBC GPFS service charge', verified = 1 WHERE bank_txn_id = 591;

-- Wave bill 694: April 2025 $65 account fee -> bank txn 361
INSERT OR IGNORE INTO wave_matches (wave_bill_id, bank_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (694, 361, 'BANK_DEBIT', 'EXACT', 'manual', 0, 'April 2025 account fee');
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, explanation, verified)
VALUES (361, 'BANK_FEE', 'April 2025 monthly account fee', 1);

-- Wave bill 703: May 2025 $5 transfer fee -> bank txn 345
INSERT OR IGNORE INTO wave_matches (wave_bill_id, bank_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (703, 345, 'BANK_DEBIT', 'EXACT', 'manual', 0, 'May 2025 transfer fee');
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, explanation, verified)
VALUES (345, 'BANK_FEE', 'May 2025 full-service transfer fee', 1);

-- Wave bill 486: Costco $654.74 split - $400 MC + $254.74 e-transfer to Dwayne
INSERT OR IGNORE INTO wave_matches (wave_bill_id, cc_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (486, 3326, 'CC_PURCHASE', 'HIGH', 'manual', 25474, 'Split payment: $400 MC + $254.74 e-transfer reimburse to Dwayne');
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (486, 'CC', 3326, 40000);
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (486, 'BANK', 777, 25474);
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, entity, explanation, verified)
VALUES (777, 'REIMBURSEMENT', 'DWAYNE', 'Costco split payment reimburse - bill 486', 1);

-- Wave bill 486 Costco split: Link MC payment (bank txn 714) to the wave bill
INSERT OR IGNORE INTO bank_allocations (bank_txn_id, target_type, target_id, amount_cents, notes)
VALUES (714, 'WAVE_BILL', 486, 40000, 'MC payment for Costco split - $400 portion');
INSERT OR IGNORE INTO cc_payment_links (bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days)
VALUES (714, 3326, 40000, '154', 0);

-- Wave bill 512: Costco $812.21 split - $412.21 debit + $400 e-transfer to Dwayne
INSERT OR IGNORE INTO wave_matches (wave_bill_id, bank_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (512, 764, 'BANK_DEBIT', 'HIGH', 'manual', 40000, 'Split: $412.21 debit + $400 e-transfer reimburse to Dwayne for MC');
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (512, 'BANK', 764, 41221);
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (512, 'BANK', 716, 40000);
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, entity, explanation, verified)
VALUES (716, 'REIMBURSEMENT', 'DWAYNE', 'Costco split - reimburse for MC payment - bill 512', 1);

-- Wave bill 575: Costco $566.01 split - $400 MC + $166.01 cash reimbursed to Dwayne
INSERT OR IGNORE INTO wave_matches (wave_bill_id, cc_txn_id, match_type, confidence, match_method, amount_diff_cents, notes)
VALUES (575, 3131, 'CC_PURCHASE', 'HIGH', 'manual', 16601, 'Split: $400 MC + $166.01 cash reimbursed to Dwayne');
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (575, 'CC', 3131, 40000);
INSERT OR IGNORE INTO split_payments (wave_bill_id, txn_type, txn_id, amount_cents) VALUES (575, 'BANK', 611, 16601);
INSERT OR IGNORE INTO cc_payment_links (bank_txn_id, cc_txn_id, amount_cents, card_last4, date_diff_days)
VALUES (612, 3131, 40000, '154', 0);
INSERT OR IGNORE INTO bank_allocations (bank_txn_id, target_type, target_id, amount_cents, notes)
VALUES (612, 'WAVE_BILL', 575, 40000, 'MC payment for Costco split');
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, entity, explanation, verified)
VALUES (611, 'REIMBURSEMENT', 'DWAYNE', 'Costco split - cash portion reimburse - bill 575', 1);


-- Bulk upgrade all LOW confidence matches to HIGH (user verified 2026-01-15)
UPDATE wave_matches SET confidence = 'HIGH' WHERE confidence = 'LOW';

-- Bank txn 363: Thomas payroll
INSERT OR REPLACE INTO bank_txn_classifications (bank_txn_id, txn_category, entity, explanation, verified)
VALUES (363, 'SHAREHOLDER_PAYROLL', 'THOMAS', 'Thomas payroll - $610.15', 1);
UPDATE bank_transactions SET manual_classification = 'SHAREHOLDER_PAYROLL', notes = 'Thomas payroll' WHERE id = 363;
DELETE FROM bank_txn_classifications WHERE bank_txn_id = 363 AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- Fix wave_matches for Superstore/Amazon bills (2026-01-15)
-- Bill 47 ($107.40 Superstore Sep 9) should match bank 1570 ($107.40)
UPDATE wave_matches SET bank_txn_id = 1570, match_type = 'CC_PAYMENT_TRANSFER' WHERE wave_bill_id = 47;

-- Bill 82 ($101.96 Superstore Oct 9) was incorrectly matched to bank 1570 - remove
UPDATE wave_matches SET bank_txn_id = NULL WHERE wave_bill_id = 82 AND bank_txn_id = 1570;

-- Bill 88 ($224.07 Superstore Oct 13) should match bank 1603 ($224.07)
UPDATE wave_matches SET bank_txn_id = 1603, match_type = 'CC_PAYMENT_TRANSFER' WHERE wave_bill_id = 88;

-- Bill 78 ($76.38 Amazon Oct 4) was incorrectly matched to bank 1529 - remove
UPDATE wave_matches SET bank_txn_id = NULL WHERE wave_bill_id = 78 AND bank_txn_id = 1529;

-- Bill 119 ($76.01 Superstore Nov 3) should match bank 1529 ($76.01)
UPDATE wave_matches SET bank_txn_id = 1529, match_type = 'CC_PAYMENT_TRANSFER' WHERE wave_bill_id = 119;

-- Bill 120 ($110.92 Superstore Nov 4) - exact match to CC payment
UPDATE wave_matches SET bank_txn_id = 1518, match_type = 'CC_PAYMENT_TRANSFER' WHERE wave_bill_id = 120;

-- Tag the GFS cash COGS placeholder with a stable invoice_number so it can be referenced from cc_chain_explanations.csv
UPDATE wave_bills
SET invoice_number = 'STUB-GFS-CASH-COGS-20231011'
WHERE source_row IS NULL
  AND invoice_number IS NULL
  AND invoice_date = '2023-10-11'
  AND vendor_raw = 'GFS - Bill'
  AND total_cents = 40000;

-- Tag Interac debit COGS placeholders with stable invoice_number values (for cc_chain_explanations.csv)
UPDATE wave_bills
SET invoice_number = 'STUB-WALMART-COGS-20230814'
WHERE source_row IS NULL
  AND invoice_number IS NULL
  AND invoice_date = '2023-08-14'
  AND vendor_raw = 'Walmart - Bill'
  AND total_cents = 3447;

UPDATE wave_bills
SET invoice_number = 'STUB-DOLLARAMA-COGS-20230814'
WHERE source_row IS NULL
  AND invoice_number IS NULL
  AND invoice_date = '2023-08-14'
  AND vendor_raw = 'Dollarama - Bill'
  AND total_cents = 5014;

-- Ensure those placeholders are matched to the correct bank Interac debits (they were previously mis-linked)
UPDATE wave_matches
SET match_type = 'BANK_DEBIT',
    bank_txn_id = 1679,
    match_method = 'USER_MANUAL',
    confidence = 'HIGH',
    date_diff_days = 0,
    amount_diff_cents = 0,
    notes = 'Interac debit COGS purchase (Walmart) - no HST captured in Wave'
WHERE wave_bill_id = (SELECT id FROM wave_bills WHERE invoice_number = 'STUB-WALMART-COGS-20230814' LIMIT 1);

UPDATE wave_matches
SET match_type = 'BANK_DEBIT',
    bank_txn_id = 1680,
    match_method = 'USER_MANUAL',
    confidence = 'HIGH',
    date_diff_days = 0,
    amount_diff_cents = 0,
    notes = 'Interac debit COGS purchase (Dollarama) - no HST captured in Wave'
WHERE wave_bill_id = (SELECT id FROM wave_bills WHERE invoice_number = 'STUB-DOLLARAMA-COGS-20230814' LIMIT 1);

UPDATE bank_transactions SET used = 1 WHERE id IN (1679, 1680);

-- === 2026-01-20: Clean up remaining SHAREHOLDER_UNMATCHED e-transfers that are already linked to Wave bills ===
-- Rationale: Many shareholder e-transfers were manually linked via wave_matches / wave_bill_funding, but the
-- bank_txn_classifications row stayed as SHAREHOLDER_UNMATCHED. This keeps review queues noisy and makes it
-- harder to see what truly lacks documentation.

-- Fix a known bad auto-match: Wave bill 538 (Atlantic Superstore $400) was incorrectly matched to a CC payment.
-- It should be linked to the shareholder reimbursement e-transfer (bank_txn_id 716).
UPDATE wave_matches
SET match_type = 'E_TRANSFER_REIMBURSE',
    bank_txn_id = 716,
    match_method = 'USER_MANUAL',
    confidence = 'HIGH',
    date_diff_days = 1,
    amount_diff_cents = 0,
    notes = 'Dwayne reimbursement (Atlantic Superstore) - linked away from CC payment'
WHERE wave_bill_id = 538;

-- Convert SHAREHOLDER_UNMATCHED → REIMBURSEMENT / RENT_REIMBURSEMENT when a Wave link exists.
UPDATE bank_txn_classifications
SET
  wave_bill_ids = (
    SELECT group_concat(DISTINCT wave_bill_id)
    FROM (
      SELECT wave_bill_id FROM wave_matches WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
      UNION ALL
      SELECT wave_bill_id FROM wave_bill_funding WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
    )
  ),
  txn_category = (
    CASE
      WHEN EXISTS (
        SELECT 1
        FROM (
          SELECT wave_bill_id FROM wave_matches WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
          UNION ALL
          SELECT wave_bill_id FROM wave_bill_funding WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
        ) l
        JOIN wave_bills wb ON wb.id = l.wave_bill_id
        WHERE lower(coalesce(wb.vendor_normalized, wb.vendor_raw, '')) LIKE '%town of amherst%'
      )
      THEN 'RENT_REIMBURSEMENT'
      ELSE 'REIMBURSEMENT'
    END
  ),
  explanation = (
    'Linked to Wave bill(s): ' ||
    COALESCE((
      SELECT group_concat(DISTINCT l.wave_bill_id)
      FROM (
        SELECT wave_bill_id FROM wave_matches WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
        UNION ALL
        SELECT wave_bill_id FROM wave_bill_funding WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
      ) l
    ), '')
  ),
  verified = 1
WHERE txn_category = 'SHAREHOLDER_UNMATCHED'
  AND EXISTS (
    SELECT 1 FROM wave_matches WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
    UNION ALL
    SELECT 1 FROM wave_bill_funding WHERE bank_txn_id = bank_txn_classifications.bank_txn_id
  );

-- Remove known incorrect Costco split classification for bank_txn_id 716 (it should be Superstore reimbursement).
DELETE FROM bank_txn_classifications
WHERE bank_txn_id = 716
  AND txn_category = 'REIMBURSEMENT'
  AND explanation = 'Costco split - reimburse for MC payment - bill 512';

-- If any bank txn has both a resolved classification and a leftover SHAREHOLDER_UNMATCHED row, drop the leftover.
DELETE FROM bank_txn_classifications
WHERE txn_category = 'SHAREHOLDER_UNMATCHED'
  AND bank_txn_id IN (611, 777);

-- Further narrow down remaining SHAREHOLDER_UNMATCHED where we have explicit notes (still unverified).
UPDATE bank_txn_classifications
SET txn_category = 'PAYROLL_REIMBURSE',
    explanation = 'Payroll remittance reimbursement (per note) - needs CRA remittance support',
    verified = 0
WHERE bank_txn_id = 1365
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_txn_classifications
SET txn_category = 'SHAREHOLDER_PAYROLL',
    explanation = 'Thomas payroll (per note) - needs payroll support',
    verified = 0
WHERE bank_txn_id IN (1255, 1237)
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- "Change"/till float funding via shareholder (not an expense): treat as CASH_WITHDRAWAL for now (unverified).
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Till/change float funding (per note) - not an expense - track against cash on hand',
    verified = 0
WHERE bank_txn_id IN (1508, 1110, 1080, 1063, 1064, 997, 998)
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User confirmation: 2023-11-06 $265 e-transfer was canteen change float.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change float (confirmed)',
    verified = 1
WHERE bank_txn_id = 1526
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User confirmation: 2023-10-23 $200 + $95 e-transfers were change reimbursements.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id IN (1568, 1569)
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User confirmation: 2023-12-11 $36.50 e-transfer (Thomas) was reimbursement for change.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id = 1450
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User confirmation: 2023-12-11 $148 + $100 e-transfers were canteen change.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id IN (1451, 1452)
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User confirmation: 2023-12-27 $2,000 e-transfer to Thomas was employee payroll (paid via Thomas).
UPDATE bank_txn_classifications
SET txn_category = 'EMPLOYEE_PAYROLL',
    entity = 'EMPLOYEE',
    explanation = 'Employee payroll (paid via Thomas) - confirmed',
    verified = 1
WHERE bank_txn_id = 1431
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_transactions
SET manual_classification = 'EMPLOYEE_PAYROLL',
    notes = COALESCE(notes, 'Employee payroll (paid via Thomas) - confirmed')
WHERE id = 1431;

-- User confirmation: 2024-12-20 + 2024-12-31 $1,500 e-transfers to Thomas were employee payroll (paid via Thomas).
UPDATE bank_txn_classifications
SET txn_category = 'EMPLOYEE_PAYROLL',
    entity = 'EMPLOYEE',
    explanation = 'Employee payroll (paid via Thomas) - confirmed',
    verified = 1
WHERE bank_txn_id IN (718, 697)
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_transactions
SET manual_classification = 'EMPLOYEE_PAYROLL',
    notes = COALESCE(notes, 'Employee payroll (paid via Thomas) - confirmed')
WHERE id IN (718, 697);

-- User confirmation: 2025-03-14 $500 e-transfer (Dwayne) was canteen change.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id = 483
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

-- User note: 2024-12-20 $12.21 e-transfer to Dwayne was a Costco partial payment correction.
UPDATE bank_txn_classifications
SET txn_category = 'REIMBURSEMENT',
    explanation = 'Costco partial payment correction (confirmed)',
    verified = 1
WHERE bank_txn_id = 715
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_transactions
SET manual_classification = 'REIMBURSEMENT',
    notes = COALESCE(notes, 'Costco partial payment correction (confirmed)')
WHERE id = 715;

-- User confirmation: 2024-02-26 $72.02 e-transfer to Thomas was payroll arrears paid by Thomas and reimbursed.
UPDATE bank_txn_classifications
SET txn_category = 'PAYROLL_REIMBURSE',
    explanation = 'Payroll arrears reimbursement (paid via Thomas) - confirmed',
    verified = 1
WHERE bank_txn_id = 1277
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_transactions
SET manual_classification = 'PAYROLL_REIMBURSE',
    notes = COALESCE(notes, 'Payroll arrears reimbursement (paid via Thomas) - confirmed')
WHERE id = 1277;

-- User confirmation: 2025-01-17 $500 e-transfer (Dwayne) was change reimbursement.
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id = 641
  AND txn_category = 'SHAREHOLDER_UNMATCHED';

UPDATE bank_transactions
SET manual_classification = 'CASH_WITHDRAWAL',
    notes = COALESCE(notes, 'Canteen change reimbursement (confirmed)')
WHERE id = 641;

-- Feb 24, 2025 deposit exception: $15,070 deposit included $5,070 that was never business cash.
-- The same-day internal transfer out $5,070 is the correction leg and should be treated as DEPOSIT_CORRECTION.
UPDATE bank_txn_classifications
SET txn_category = 'DEPOSIT_CORRECTION',
    entity = 'CORP',
    explanation = 'Deposit correction: $5,070 transferred out same day as $15,070 deposit (business cash was $10,000) - confirmed',
    verified = 1
WHERE bank_txn_id = 540
  AND txn_category IN ('INTERNAL_TRANSFER', 'DEPOSIT_CORRECTION');

UPDATE bank_transactions
SET manual_classification = 'DEPOSIT_CORRECTION',
    notes = COALESCE(notes, 'Deposit correction: $5,070 transferred out same day as $15,070 deposit (business cash was $10,000) - confirmed')
WHERE id = 540;

-- Ensure existing notes get appended (not blocked by COALESCE).
UPDATE bank_transactions
SET notes = CASE
  WHEN notes IS NULL OR trim(notes) = '' THEN 'Deposit correction: $5,070 transferred out same day as $15,070 deposit (business cash was $10,000) - confirmed'
  WHEN notes LIKE '%Deposit correction:%' THEN notes
  ELSE notes || ' | Deposit correction: $5,070 transferred out same day as $15,070 deposit (business cash was $10,000) - confirmed'
END
WHERE id = 540;

-- === 2026-01-20: Clear remaining "high risk" review items that are now confirmed ===
-- Change/till float reimbursements (confirmed)
UPDATE bank_txn_classifications
SET txn_category = 'CASH_WITHDRAWAL',
    explanation = 'Canteen change reimbursement (confirmed)',
    verified = 1
WHERE bank_txn_id IN (998, 997, 1064, 1063, 1080, 1110, 1508)
  AND txn_category = 'CASH_WITHDRAWAL';

UPDATE bank_transactions
SET manual_classification = 'CASH_WITHDRAWAL',
    notes = CASE
      WHEN notes IS NULL OR trim(notes) = '' THEN 'Canteen change reimbursement (confirmed)'
      WHEN notes LIKE '%Canteen change reimbursement (confirmed)%' THEN notes
      ELSE notes || ' | Canteen change reimbursement (confirmed)'
    END
WHERE id IN (998, 997, 1064, 1063, 1080, 1110, 1508);

-- Payroll remittance reimbursements to Thomas (confirmed)
UPDATE bank_txn_classifications
SET txn_category = 'PAYROLL_REIMBURSE',
    entity = 'THOMAS',
    explanation = 'Payroll remittance reimbursement (paid via Thomas) - confirmed',
    verified = 1
WHERE bank_txn_id IN (1255, 1237)
  AND txn_category = 'SHAREHOLDER_PAYROLL';

UPDATE bank_transactions
SET manual_classification = 'PAYROLL_REIMBURSE',
    notes = CASE
      WHEN notes IS NULL OR trim(notes) = '' THEN 'Payroll remittance reimbursement (paid via Thomas) - confirmed'
      WHEN notes LIKE '%Payroll remittance reimbursement (paid via Thomas) - confirmed%' THEN notes
      ELSE notes || ' | Payroll remittance reimbursement (paid via Thomas) - confirmed'
    END
WHERE id IN (1255, 1237);

-- HST reimbursement to Thomas (confirmed category; period details uncertain).
UPDATE bank_txn_classifications
SET txn_category = 'HST_REIMBURSEMENT',
    entity = 'THOMAS',
    explanation = 'HST reimbursement to Thomas - used to clear balance and pay Q3 (confirmed, exact period TBD)',
    verified = 1
WHERE bank_txn_id = 909
  AND txn_category = 'HST_REIMBURSEMENT';

UPDATE bank_transactions
SET manual_classification = 'HST_REIMBURSEMENT',
    notes = CASE
      WHEN notes IS NULL OR trim(notes) = '' THEN 'HST reimbursement to Thomas - used to clear balance and pay Q3 (confirmed, exact period TBD)'
      WHEN notes LIKE '%HST reimbursement to Thomas - used to clear balance and pay Q3%' THEN notes
      ELSE notes || ' | HST reimbursement to Thomas - used to clear balance and pay Q3 (confirmed, exact period TBD)'
    END
WHERE id = 909;

-- === Data hygiene: deduplicate patch-driven tables (01e_apply_manual_patch.py is not idempotent for these) ===
-- wave_bill_funding: keep a single row per logical funding line; prefer the most-informative notes.
DELETE FROM wave_bill_funding
WHERE id != (
  SELECT w2.id
  FROM wave_bill_funding w2
  WHERE w2.wave_bill_id = wave_bill_funding.wave_bill_id
    AND w2.funding_type = wave_bill_funding.funding_type
    AND (
      (w2.bank_txn_id IS NULL AND wave_bill_funding.bank_txn_id IS NULL)
      OR (w2.bank_txn_id = wave_bill_funding.bank_txn_id)
    )
    AND w2.amount_cents = wave_bill_funding.amount_cents
  ORDER BY length(coalesce(w2.notes, '')) DESC, w2.id ASC
  LIMIT 1
);

-- Prevent future duplicate inserts (covers NULL/non-NULL bank_txn_id separately).
CREATE UNIQUE INDEX IF NOT EXISTS uq_wave_bill_funding_with_bank
ON wave_bill_funding(wave_bill_id, funding_type, bank_txn_id, amount_cents)
WHERE bank_txn_id IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS uq_wave_bill_funding_no_bank
ON wave_bill_funding(wave_bill_id, funding_type, amount_cents)
WHERE bank_txn_id IS NULL;

-- cash_reimbursements: keep a single row per logical reimbursement line; prefer the most-informative notes.
DELETE FROM cash_reimbursements
WHERE id != (
  SELECT c2.id
  FROM cash_reimbursements c2
  WHERE c2.wave_bill_id = cash_reimbursements.wave_bill_id
    AND (
      (c2.cc_txn_id IS NULL AND cash_reimbursements.cc_txn_id IS NULL)
      OR (c2.cc_txn_id = cash_reimbursements.cc_txn_id)
    )
    AND c2.reimbursed_to = cash_reimbursements.reimbursed_to
    AND c2.amount_cents = cash_reimbursements.amount_cents
    AND (
      (c2.reimbursement_date IS NULL AND cash_reimbursements.reimbursement_date IS NULL)
      OR (c2.reimbursement_date = cash_reimbursements.reimbursement_date)
    )
  ORDER BY length(coalesce(c2.notes, '')) DESC, c2.id ASC
  LIMIT 1
);

-- Prevent future duplicate inserts (covers NULL/non-NULL cc_txn_id and NULL/non-NULL reimbursement_date).
CREATE UNIQUE INDEX IF NOT EXISTS uq_cash_reimb_cc_date
ON cash_reimbursements(wave_bill_id, cc_txn_id, reimbursed_to, amount_cents, reimbursement_date)
WHERE cc_txn_id IS NOT NULL AND reimbursement_date IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS uq_cash_reimb_cc_nodate
ON cash_reimbursements(wave_bill_id, cc_txn_id, reimbursed_to, amount_cents)
WHERE cc_txn_id IS NOT NULL AND reimbursement_date IS NULL;

CREATE UNIQUE INDEX IF NOT EXISTS uq_cash_reimb_nocc_date
ON cash_reimbursements(wave_bill_id, reimbursed_to, amount_cents, reimbursement_date)
WHERE cc_txn_id IS NULL AND reimbursement_date IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS uq_cash_reimb_nocc_nodate
ON cash_reimbursements(wave_bill_id, reimbursed_to, amount_cents)
WHERE cc_txn_id IS NULL AND reimbursement_date IS NULL;

-- -------------------------------------------------------------------
-- VERIFIED CLARIFICATIONS (POST-AUDIT CLEANUP)
-- -------------------------------------------------------------------

-- Amherst Ducks e-transfers were confirmed as employee payroll (not revenue returns).
UPDATE bank_txn_classifications
SET
  txn_category = 'EMPLOYEE_PAYROLL',
  entity = 'EMPLOYEE',
  verified = 1,
  explanation = 'Employee payroll e-transfer (recipient: Amherst Ducks)'
WHERE bank_txn_id IN (639, 757, 770, 830);

-- One-off e-transfers that are already backed by Wave bills (via wave_bill_funding).
UPDATE bank_txn_classifications
SET
  txn_category = 'VENDOR_ETRANSFER',
  entity = 'VENDOR',
  verified = 1,
  explanation = 'Markis Bus Tours payment (Wave bill 277)'
WHERE bank_txn_id = 1182;

UPDATE bank_txn_classifications
SET
  txn_category = 'VENDOR_ETRANSFER',
  entity = 'VENDOR',
  verified = 1,
  explanation = 'Facebook Marketplace merchandising (Wave bill 725)'
WHERE bank_txn_id = 1128;

UPDATE bank_txn_classifications
SET
  txn_category = 'VENDOR_ETRANSFER',
  entity = 'VENDOR',
  verified = 1,
  explanation = 'Underground Graffix stickers (Wave bill 730)'
WHERE bank_txn_id = 809;

UPDATE bank_txn_classifications
SET
  txn_category = 'DONATION',
  entity = 'CORP',
  verified = 1,
  explanation = 'U9 Dev Hockey donation (Wave bill 726)'
WHERE bank_txn_id = 737;

-- Correction: Amherst Ducks e-transfers were ticket revenue payouts (not payroll).
UPDATE bank_txn_classifications
SET
  txn_category = 'DUCKS_REVENUE_RETURN',
  entity = 'VENDOR',
  verified = 1,
  explanation = 'Amherst Ducks ticket sales payout (online ticket sales remitted)'
WHERE bank_txn_id IN (639, 757, 770, 830);

UPDATE bank_transactions
SET
  manual_classification = 'VENDOR_PAYMENT',
  notes = 'Amherst Ducks ticket sales payout (online ticket sales remitted)'
WHERE id IN (639, 757, 770, 830);

-- -------------------------------------------------------------------
-- BATCH A CONFIRMATIONS (PAYROLL REIMBURSEMENTS / PAYROLL)
-- -------------------------------------------------------------------

-- Confirmed: 292.23 was a payroll reimbursement for January.
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Payroll reimbursement for January (confirmed)'
WHERE bank_txn_id = 1276;

UPDATE bank_transactions
SET
  manual_classification = 'PAYROLL_REIMBURSE',
  notes = 'Payroll reimbursement for January (confirmed)'
WHERE id = 1276;

-- Confirmed: both 1250 e-transfers to Thomas were payroll (Thomas payroll).
UPDATE bank_txn_classifications
SET
  txn_category = 'SHAREHOLDER_PAYROLL',
  entity = 'THOMAS',
  verified = 1,
  explanation = 'Thomas payroll - $1250.00 (confirmed)'
WHERE bank_txn_id IN (384, 482);

UPDATE bank_transactions
SET
  manual_classification = 'SHAREHOLDER_PAYROLL',
  notes = 'Thomas payroll - $1250.00 (confirmed)'
WHERE id IN (384, 482);

-- Verified via CRA payroll export (CanteenPayrollTransactions.csv) exact amount + date matches.
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Payroll reimbursement, matches CRA export Payment Dec 2023 late ($1519.31) + Payment Sept 2023 late ($22.10), received 2024-01-22'
WHERE bank_txn_id = 1365;

UPDATE bank_transactions
SET
  manual_classification = 'PAYROLL_REIMBURSE',
  notes = 'Verified vs CRA payroll export, received 2024-01-22'
WHERE id = 1365;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Payroll reimbursement, matches CRA export Payment Mar 2024, received 2024-04-02'
WHERE bank_txn_id = 1178;

UPDATE bank_transactions
SET
  manual_classification = 'PAYROLL_REIMBURSE',
  notes = 'Verified vs CRA payroll export: Payment Mar 2024'
WHERE id = 1178;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Payroll reimbursement, matches CRA export Payment Apr 2024, received 2024-05-01'
WHERE bank_txn_id = 1122;

UPDATE bank_transactions
SET
  manual_classification = 'PAYROLL_REIMBURSE',
  notes = 'Verified vs CRA payroll export: Payment Apr 2024'
WHERE id = 1122;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Payroll reimbursement, matches CRA export Payment Sept 2024, received 2024-10-07'
WHERE bank_txn_id = 965;

UPDATE bank_transactions
SET
  manual_classification = 'PAYROLL_REIMBURSE',
  notes = 'Verified vs CRA payroll export: Payment Sept 2024'
WHERE id = 965;

-- -------------------------------------------------------------------
-- CRA DIRECT REMITTANCES (PAYROLL + GST/HST) - VERIFIED VIA CRA EXPORTS
-- -------------------------------------------------------------------

-- Payroll remittances (direct debit memo) verified via CRA payroll export.
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Nov 2024 (CRA received 2024-12-05)'
WHERE bank_txn_id = 761;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Nov 2024 (CRA received 2024-12-05)'
WHERE id = 761;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Dec 2024 (CRA received 2025-01-15)'
WHERE bank_txn_id = 657;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Dec 2024 (CRA received 2025-01-15)'
WHERE id = 657;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Jan 2025 (CRA received 2025-02-11)'
WHERE bank_txn_id = 568;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Jan 2025 (CRA received 2025-02-11)'
WHERE id = 568;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Feb 2025 (CRA received 2025-03-04)'
WHERE bank_txn_id = 503;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Feb 2025 (CRA received 2025-03-04)'
WHERE id = 503;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Late year-end payment 2024 (CRA received 2025-03-04)'
WHERE bank_txn_id = 504;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Late year-end payment 2024 (CRA received 2025-03-04)'
WHERE id = 504;

-- Arrears payment (direct debit memo) verified via CRA arrears export.
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll arrears payment (CRA received 2025-03-17)'
WHERE bank_txn_id = 458;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll arrears payment (CRA received 2025-03-17)'
WHERE id = 458;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Mar 2025 (CRA received 2025-04-14)'
WHERE bank_txn_id = 387;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Mar 2025 (CRA received 2025-04-14)'
WHERE id = 387;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment Apr 2025 (CRA received 2025-05-06)'
WHERE bank_txn_id = 352;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance: Payment Apr 2025 (CRA received 2025-05-06)'
WHERE id = 352;

-- GST/HST remittances: these were previously parked under PAYROLL_REMIT; reclassify + verify via CRA HST export.
UPDATE bank_txn_classifications
SET
  txn_category = 'GST_HST_REMIT',
  entity = 'CORP',
  verified = 1,
  explanation = 'CRA GST/HST payment for period end 2024-06-30 (posted 2024-11-18)'
WHERE bank_txn_id = 834;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA GST/HST payment (period end 2024-06-30)'
WHERE id = 834;

UPDATE bank_txn_classifications
SET
  txn_category = 'GST_HST_REMIT',
  entity = 'CORP',
  verified = 1,
  explanation = 'CRA GST/HST payment for period end 2024-03-31 (posted 2024-11-18)'
WHERE bank_txn_id = 835;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA GST/HST payment (period end 2024-03-31)'
WHERE id = 835;

UPDATE bank_txn_classifications
SET
  txn_category = 'GST_HST_REMIT',
  entity = 'CORP',
  verified = 1,
  explanation = 'CRA GST/HST payment for period end 2024-09-30 (posted 2024-12-04)'
WHERE bank_txn_id = 798;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA GST/HST payment (period end 2024-09-30)'
WHERE id = 798;

UPDATE bank_txn_classifications
SET
  txn_category = 'GST_HST_REMIT',
  entity = 'CORP',
  verified = 1,
  explanation = 'CRA GST/HST payment for period end 2024-12-31 (posted 2025-04-25)'
WHERE bank_txn_id = 375;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA GST/HST payment (period end 2024-12-31)'
WHERE id = 375;

UPDATE bank_txn_classifications
SET
  txn_category = 'GST_HST_REMIT',
  entity = 'CORP',
  verified = 1,
  explanation = 'CRA GST/HST payment for period end 2025-03-31 (posted 2025-07-02)'
WHERE bank_txn_id = 298;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA GST/HST payment (period end 2025-03-31)'
WHERE id = 298;

-- GPFS service charges are bank fees, not remittances.
UPDATE bank_txn_classifications
SET
  txn_category = 'BANK_FEE',
  entity = 'CORP',
  verified = 1,
  explanation = 'CIBC GPFS service charge'
WHERE bank_txn_id IN (360, 416, 505, 689, 789);

UPDATE bank_transactions
SET
  manual_classification = 'BANK_FEE',
  notes = 'CIBC GPFS service charge'
WHERE id IN (360, 416, 505, 689, 789);

-- Post-FY payroll remittances (still useful to have verified for continuity).
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment May 2025 (CRA received 2025-06-04)'
WHERE bank_txn_id = 330;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'CRA payroll remittance: Payment July 2025 (CRA received 2025-08-07)'
WHERE bank_txn_id = 279;

UPDATE bank_transactions
SET
  manual_classification = 'CRA_PAYMENT',
  notes = 'CRA payroll remittance (verified via CRA payroll export)'
WHERE id IN (279, 330);

-- Bank txn 909 (2024-10-22): $3,000 e-transfer to Thomas includes:
-- - $2,000 CRA HST payment (non-reporting period; see CRA export), and
-- - two $500 cash COGS purchases from GFS (Cheese Curds) reimbursed to Thomas.
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
SELECT wb.id, 'BANK_DIRECT', 909, 50000, 'GFS cheese curds cash COGS reimbursed to Thomas (split of $3,000 e-transfer)'
FROM wave_bills wb
WHERE wb.invoice_number = 'STUB-GFS-CASH-COGS-20241022-1'
  AND NOT EXISTS (
    SELECT 1 FROM wave_bill_funding wbf
    WHERE wbf.wave_bill_id = wb.id AND wbf.funding_type = 'BANK_DIRECT' AND wbf.bank_txn_id = 909 AND wbf.amount_cents = 50000
  );

INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
SELECT wb.id, 'BANK_DIRECT', 909, 50000, 'GFS cheese curds cash COGS reimbursed to Thomas (split of $3,000 e-transfer)'
FROM wave_bills wb
WHERE wb.invoice_number = 'STUB-GFS-CASH-COGS-20241022-2'
  AND NOT EXISTS (
    SELECT 1 FROM wave_bill_funding wbf
    WHERE wbf.wave_bill_id = wb.id AND wbf.funding_type = 'BANK_DIRECT' AND wbf.bank_txn_id = 909 AND wbf.amount_cents = 50000
  );

UPDATE bank_txn_classifications
SET
  explanation = 'E-transfer to Thomas $3,000: $2,000 CRA HST payment (non-reporting) + 2x $500 GFS cheese curds cash COGS (no tax placeholders)',
  wave_bill_ids = (
    SELECT CAST(wb1.id AS TEXT) || ',' || CAST(wb2.id AS TEXT)
    FROM wave_bills wb1, wave_bills wb2
    WHERE wb1.invoice_number = 'STUB-GFS-CASH-COGS-20241022-1'
      AND wb2.invoice_number = 'STUB-GFS-CASH-COGS-20241022-2'
  )
WHERE bank_txn_id = 909;

UPDATE bank_transactions
SET
  notes = 'E-transfer to Thomas $3,000: $2,000 CRA HST payment (non-reporting) + 2x $500 GFS cheese curds cash COGS (no tax placeholders)'
WHERE id = 909;

-- Rent reimbursements: clarify early rent transfers.
-- Bank txn 1639: June 2023 full rent reimbursed to Dwayne ($700 + $105 HST = $805).
UPDATE bank_txn_classifications
SET
  explanation = 'Rent reimbursement to Dwayne for June 2023 Town of Amherst full rent ($700 + $105 HST = $805)',
  verified = 1,
  wave_bill_ids = '1'
WHERE bank_txn_id = 1639;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Dwayne for June 2023 Town of Amherst full rent ($700 + $105 HST = $805)'
WHERE id = 1639;

-- Bank txn 1689: July 2023 rent reimbursed to Dwayne via internal transfer to 00153/19-23218 ($350 + $52.50 HST = $402.50).
UPDATE bank_txn_classifications
SET
  entity = 'DWAYNE',
  txn_category = 'RENT_REIMBURSEMENT',
  explanation = 'Rent reimbursement to Dwayne for July 2023 Town of Amherst rent via transfer to 00153/19-23218 ($350 + $52.50 HST = $402.50)',
  verified = 1,
  wave_bill_ids = '13'
WHERE bank_txn_id = 1689;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Dwayne for July 2023 Town of Amherst rent via transfer to 00153/19-23218 ($350 + $52.50 HST = $402.50)'
WHERE id = 1689;

-- Remaining rent reimbursements now confirmed by user (all $402.50 are rent payments).
-- Bank txn 1382: $862.50 e-transfer to Dwayne, tied to Feb 2024 rent (prepaid).
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Rent reimbursement to Dwayne for Feb 2024 Town of Amherst rent (paid in advance)',
  wave_bill_ids = '191'
WHERE bank_txn_id = 1382;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Dwayne for Feb 2024 Town of Amherst rent (paid in advance)'
WHERE id = 1382;

-- Bank txns 1113 + 1114: two $402.50 e-transfers to Thomas on 2024-05-07 = $805 full rent (split).
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Rent reimbursement to Thomas: $402.50 split payment (1/2) toward $805 full rent (paired with bank_txn_id 1114)',
  wave_bill_ids = '323'
WHERE bank_txn_id = 1113;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Thomas: $402.50 split payment (1/2) toward $805 full rent (paired with bank_txn_id 1114)'
WHERE id = 1113;

UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Rent reimbursement to Thomas: $402.50 split payment (2/2) toward $805 full rent (paired with bank_txn_id 1113)',
  wave_bill_ids = '323'
WHERE bank_txn_id = 1114;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Thomas: $402.50 split payment (2/2) toward $805 full rent (paired with bank_txn_id 1113)'
WHERE id = 1114;

-- Bank txn 1077: $402.50 e-transfer to Dwayne on 2024-07-30 = half of $805 rent (other half via bank txn 1042 to Thomas).
UPDATE bank_txn_classifications
SET
  verified = 1,
  explanation = 'Rent reimbursement to Dwayne: $402.50 split payment (1/2) toward $805 rent (other half via bank_txn_id 1042 to Thomas)',
  wave_bill_ids = '324'
WHERE bank_txn_id = 1077;

UPDATE bank_transactions
SET
  manual_classification = 'REIMBURSEMENT',
  notes = 'Rent reimbursement to Dwayne: $402.50 split payment (1/2) toward $805 rent (other half via bank_txn_id 1042 to Thomas)'
WHERE id = 1077;

-- Bank txn 1615: reimbursement to Dwayne for a missing GFS damaged/pallet salvage invoice (oil, chicken, cheese curds).
-- Create placeholder Wave bill (via overrides/wave_bill_overrides.csv) and link here. No HST/ITC.
INSERT INTO wave_bill_funding (wave_bill_id, funding_type, bank_txn_id, amount_cents, notes)
SELECT wb.id, 'BANK_DIRECT', 1615, 86250, 'GFS damaged salvage COGS reimbursed to Dwayne (oil, chicken, cheese curds)'
FROM wave_bills wb
WHERE wb.invoice_number = 'STUB-GFS-DAMAGED-20231012'
  AND NOT EXISTS (
    SELECT 1 FROM wave_bill_funding wbf
    WHERE wbf.wave_bill_id = wb.id AND wbf.funding_type = 'BANK_DIRECT' AND wbf.bank_txn_id = 1615 AND wbf.amount_cents = 86250
  );

UPDATE bank_txn_classifications
SET
  txn_category = 'REIMBURSEMENT',
  entity = 'DWAYNE',
  verified = 1,
  explanation = 'Reimbursement to Dwayne: GFS damaged oil, chicken, cheese curds salvage COGS $862.50 (no HST placeholder)',
  wave_bill_ids = (SELECT CAST(id AS TEXT) FROM wave_bills WHERE invoice_number = 'STUB-GFS-DAMAGED-20231012')
WHERE bank_txn_id = 1615;

UPDATE bank_transactions
SET
  used = 1,
  manual_classification = 'REIMBURSEMENT',
  notes = 'Reimbursement to Dwayne: GFS damaged oil, chicken, cheese curds salvage COGS $862.50 (no HST placeholder)'
WHERE id = 1615;

-- Bank txn 353: CIBC cheque order (Deluxe) paid via PAD. Vendor is effectively CIBC.
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
SELECT 741, wb.id, 'BANK_DEBIT', 353, NULL, NULL, 'HIGH', 'MANUAL_CIBC_CHEQUE_ORDER', 0, abs(16477 - wb.total_cents), 'CIBC cheque order (Deluxe) PAD - Wave vs bank may differ by 1 cent'
FROM wave_bills wb
WHERE wb.source_row = 699;

UPDATE bank_transactions
SET
  used = 1,
  vendor_parsed = 'CIBC',
  manual_classification = 'BANK_FEE',
  notes = 'CIBC cheque order (Deluxe) - bank_txn_id=353 linked to Wave bill source_row=699'
WHERE id = 353;

-- Bank txn 1221: Capital PAD payment for invoice 2548372 (PAP email).
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
SELECT 742, wb.id, 'PAD_INVOICE', 1221, NULL, NULL, 'EXACT', 'MANUAL_CAPITAL_PAP', 16, 0, 'Capital Foods PAD payment for invoice 2548372 (PAP email)'
FROM wave_bills wb
WHERE wb.invoice_number = '2548372';

UPDATE pad_invoices
SET wave_bill_id = (SELECT id FROM wave_bills WHERE invoice_number = '2548372')
WHERE invoice_number = '2548372'
  AND pad_payment_id = (SELECT id FROM pad_payments WHERE bank_txn_id = 1221 LIMIT 1);

UPDATE bank_transactions
SET
  used = 1,
  notes = 'Capital Foods PAD payment for invoice 2548372 (PAP email)'
WHERE id = 1221;

-- Bank txn 1350: Thomas reimbursement for FB marketplace hot water heater ($40). Add placeholder Wave bill via overrides and link.
INSERT INTO wave_matches (id, wave_bill_id, match_type, bank_txn_id, cc_txn_id, cc_payment_txn_id, confidence, match_method, date_diff_days, amount_diff_cents, notes)
SELECT 743, wb.id, 'E_TRANSFER_REIMBURSE', 1350, NULL, NULL, 'EXACT', 'MANUAL_FB_HOTWATER', 0, 0, 'Thomas reimbursement: FB marketplace hot water heater ($40)'
FROM wave_bills wb
WHERE wb.invoice_number = 'FB-HOTWATER-HEATER-20240129';

UPDATE bank_txn_classifications
SET
  txn_category = 'REIMBURSEMENT',
  verified = 1,
  explanation = 'Reimbursement to Thomas: FB marketplace hot water heater ($40 no tax placeholder)',
  wave_bill_ids = (SELECT CAST(id AS TEXT) FROM wave_bills WHERE invoice_number = 'FB-HOTWATER-HEATER-20240129')
WHERE bank_txn_id = 1350;

UPDATE bank_transactions
SET
  used = 1,
  manual_classification = 'REIMBURSEMENT',
  notes = 'Reimbursement to Thomas: FB marketplace hot water heater ($40 no tax placeholder)'
WHERE id = 1350;

-- Bank txn 1151: Shopify negative payout/fee adjustment (bank debit) - handled in credits reconciliation.
UPDATE bank_txn_classifications
SET
  entity = 'CORP',
  txn_category = 'SHOPIFY_NEGATIVE_PAYOUT',
  verified = 1,
  explanation = 'Shopify negative payout (bank debit) / fee adjustment - handled in credits reconciliation',
  wave_bill_ids = NULL
WHERE bank_txn_id = 1151;

UPDATE bank_transactions
SET
  used = 1,
  manual_classification = 'SHOPIFY_NEGATIVE_PAYOUT',
  notes = 'Shopify negative payout (bank debit) / fee adjustment - handled in credits reconciliation'
WHERE id = 1151;
