P.1. CONFIRMATORY HIV TESTING [program :: HTS PROGRAM $$ scope :: TODAY $$ includejs :: touchScreenToolkit;hts]

Q.1.1. First Pass Test Kit 1 Expiry Date [pos :: 0 $$ id:: fp_lot_1_expiry $$ condition :: false]
Q.1.2. First Pass Test Kit 2 Expiry Date [pos :: 1 $$ id:: fp_lot_2_expiry $$ condition :: false]
Q.1.3. Immediate Repeat Test Kit 1 Expiry Date [pos :: 2 $$ id :: im_lot_1_expiry $$ condition :: false]
Q.1.4. Immediate Repeat Test Kit 2 Expiry Date [pos :: 3 $$ id :: im_lot_2_expiry $$ condition :: false]

Q.1.5. First Pass Test Kit 1 Dispatch ID [pos :: 4 $$ id :: fp_lot_1_dispatch_id $$ condition :: false]
Q.1.6. First Pass Test Kit 2 Dispatch ID [pos :: 5 $$ id :: fp_lot_2_dispatch_id $$ condition :: false]
Q.1.7. Immediate Repeat Test Kit 1 Dispatch ID [pos :: 6 $$ id :: im_lot_1_dispatch_id $$ condition :: false]
Q.1.8. Immediate Repeat Test Kit 2 Dispatch ID [pos :: 7 $$ id :: im_lot_2_dispatch_id $$ condition :: false]

Q.1.9. Client gives consent to be tested? [pos :: 8 $$ id :: consent $$ tt_onLoad :: setTestKits() $$ condition :: evalCondition(-1) && !((evalCondition(3) || evalCondition(-2)) && !evalCondition(-3) && !evalCondition(4))]
O.1.9.1. Yes
O.1.9.2. No

C.1.10. First Pass Test 1 Kit Category [pos :: 9 $$ tt_onUnload :: setAjaxUrl(3) $$ ajaxURL :: /stock/stock_categories?category= $$ condition :: evalCondition(0) $$ condition :: false]

Q.1.11. First Pass Test Kit 1 Name [pos :: 10 $$ id :: fp_item_name1 $$ tt_onUnload :: setAjaxUrl(4) $$ condition :: evalCondition(0) $$ field_type :: hidden]

Q.1.12. First Pass Test Kit 1 Lot Number [pos :: 11 $$ id :: fp_lot_number1 $$ expiry :: fp_lot_1_expiry $$ dispatch :: fp_lot_1_dispatch_id $$ tt_onUnLoad :: validateExpiryDate(__$('touchscreenInput' + tstCurrentPage).value, "fp_lot_1_dispatch_id") $$ condition :: __$("consent").value.trim() != "No"]

Q.1.13. First Pass Test 1 Result [pos :: 12 $$ id :: fp_test1_result $$ tt_onLoad :: setTestKits(); loadSerialTest(__$("fp_test1_result"), __$("fp_test1_duration"), __$("fp_item_name1").value.trim(), "First Pass") $$ field_type :: hidden $$ tt_pageStyleClass :: NoControls NoKeyboard $$ optional :: true $$ tt_onUnload :: activateNavBtn() ]

C.1.14. First Pass Test 2 Kit Category [pos :: 13 $$ tt_onUnload :: setAjaxUrl(5) $$ ajaxURL :: /stock/stock_categories?category= $$ condition :: evalCondition(2) $$ condition :: false]

Q.1.15. First Pass Test Kit 2 Name [pos :: 14 $$ id :: fp_item_name2 $$ tt_onUnload :: setAjaxUrl(6) $$ condition :: evalCondition(2) $$ field_type :: hidden]

Q.1.16. First Pass Test Kit 2 Lot Number [pos :: 15 $$ id :: fp_lot_number2 $$ expiry :: fp_lot_2_expiry $$ dispatch :: fp_lot_2_dispatch_id $$ tt_onUnLoad :: validateExpiryDate(__$('touchscreenInput' + tstCurrentPage).value, "fp_lot_2_dispatch_id"); $$ condition :: __$("consent").value.trim() != "No" ]

Q.1.17. First Pass Test 2 Result [pos :: 16 $$ id :: fp_test2_result $$ field_type :: hidden $$ tt_pageStyleClass :: NoControls NoKeyboard $$ optional :: true $$ tt_onUnload :: clearTimers("HIV TESTING"); activateNavBtn();]

Q.1.18. First Pass Test 1 & Test 2 Parallel Tests [pos :: 17 $$ id :: fp_parallel $$ tt_onLoad :: if(__$("backButton")) __$("backButton").style.display = "none"; setTestKits(function(){ recommendedTimerForLabels([__$("fp_item_name1").value, __$("fp_item_name2").value]); loadPassParallelTests(__$("fp_test1_result"), __$("fp_test1_duration"), __$("fp_test2_result"), __$("fp_test2_duration"),window.parent.dashboard.data.kits['First Test'], window.parent.dashboard.data.kits['Second Test'],"First Parallel"); })  $$ condition :: __$("consent").value.trim() != "No" $$ tt_pageStyleClass:: NoControls NoKeyboard$$ optional:: true $$ tt_onUnload :: removeParallelTests(); activateNavBtn() $$ helpText :: First Pass Test 1 & Test 2 Parallel]

Q.1.19. Immediate Repeat Tester [pos :: 18 $$ id :: im_tester $$ condition :: evalCondition(5) && !evalCondition(-3) $$ ajaxURL :: /list_users?name= $$ tt_onLoad :: activateNavBtn()]

Q.1.20. Immediate Tester's Password [pos :: 19 $$ condition :: evalCondition(5) && !evalCondition(-3) $$ tt_onLoad :: checkValidation() $$ tt_onUnLoad :: stopValidationChecks() $$ textCase :: lower $$ type :: password]

Q.1.21. Immediate Repeat Test 1 Kit Category [pos :: 20 $$ tt_onUnload :: setAjaxUrl(7) $$ ajaxURL :: /stock/stock_categories?category= $$ condition :: evalCondition(5) $$ condition :: false ]

Q.1.22. Immediate Repeat Test Kit 1 Name [pos :: 21 $$ id :: im_item_name1 $$ tt_onUnload :: setAjaxUrl(8) $$ condition :: evalCondition(5) $$ field_type :: hidden]

Q.1.23. Immediate Repeat Test Kit 1 Lot Number [pos :: 22 $$ id :: im_lot_number1 $$ expiry :: im_lot_1_expiry $$ dispatch :: im_lot_1_dispatch_id $$ condition :: evalCondition(5) && !evalCondition(-3) $$ tt_onLoad :: if(__$("im_lot_number1").getAttribute("consumption_id")){reverseConsumption(__$("im_lot_number1").getAttribute("consumption_id"),"im", "1")} $$ tt_onUnLoad :: validateExpiryDate(__$('touchscreenInput' + tstCurrentPage).value, "im_lot_1_dispatch_id")]

Q.1.24. Immediate Repeat Test 1 Result [pos :: 23 $$ id :: im_test1_result $$ condition :: false $$ tt_onLoad :: setTestKits(); ]

Q.1.25. Immediate Repeat Test 2 Kit Category [pos :: 24$$ tt_onUnload :: setAjaxUrl(9) $$ ajaxURL :: /stock/stock_categories?category= $$ condition :: evalCondition(5) $$ condition :: false]

Q.1.26. Immediate Repeat Test Kit 2 Name [pos :: 25 $$ id :: im_item_name2 $$ tt_onUnload :: setAjaxUrl(10) $$ condition :: evalCondition(5) $$ field_type :: hidden]

Q.1.27. Immediate Repeat Test Kit 2 Lot Number [pos :: 26 $$ id :: im_lot_number2 $$ expiry :: im_lot_2_expiry $$ dispatch :: im_lot_2_dispatch_id $$ condition :: evalCondition(5) && !evalCondition(-3) $$ tt_onLoad :: if(__$("im_lot_number2").getAttribute("consumption_id")){reverseConsumption(__$("im_lot_number2").getAttribute("consumption_id"),"im", "2")} $$ tt_onUnLoad :: validateExpiryDate(__$('touchscreenInput' + tstCurrentPage).value, "im_lot_2_dispatch_id")]

Q.1.28. Immediate Repeat Test 2 Result [pos :: 27 $$ id :: im_test2_result $$ condition :: false $$ tt_onLoad :: setTestKits(); ]

Q.1.29. Immediate Repeat Test 1 & Test 2 Parallel Tests [pos :: 28 $$ id :: fp_parallel $$ tt_onLoad :: if(__$("backButton")) __$("backButton").style.display = "none"; setTestKits(function(){ recommendedTimerForLabels([__$("im_item_name1").value,__$("im_item_name2").value]); loadPassParallelTests(__$("im_test1_result"), __$("im_test1_duration"), __$("im_test2_result"), __$("im_test2_duration"), __$("im_item_name1").value.trim(), __$("im_item_name2").value.trim(), "Immediate Parallel"); __$("helpText" + tstCurrentPage).innerHTML = "Immediate Repeat 1 & 2 Parallel" }) $$ condition :: evalCondition(5) $$ tt_pageStyleClass :: NoControls NoKeyboard $$ optional :: true $$ tt_onUnload :: removeParallelTests(); activateNavBtn()]

Q.1.30. First Pass Test Kit 1 Testing Duration (Minutes) 1 [pos :: 29 $$ id :: fp_test1_duration $$ field_type :: hidden $$ value :: 00:00]
Q.1.31. First Pass Test Kit 2 Testing Duration (Minutes) 1 [pos :: 30 $$ id :: fp_test2_duration $$ field_type :: hidden $$ value :: 00:00]
Q.1.32. Immediate Repeat Test Kit 1 Testing Duration (Minutes) 1 [pos :: 31 $$ id :: im_test1_duration $$ field_type :: hidden $$ value :: 00:00]
Q.1.33. Immediate Repeat Test Kit 2 Testing Duration (Minutes) 1 [pos :: 32 $$ id :: im_test2_duration $$ field_type :: hidden $$ value :: 00:00]

Q.1.34. First Pass Test Kit 1 Testing Duration (Minutes) [pos :: 33 $$ id :: fp_test1_time $$ field_type :: hidden $$ value :: 00:00]
Q.1.35. First Pass Test Kit 2 Testing Duration (Minutes) [pos :: 34 $$ id :: fp_test2_time $$ field_type :: hidden $$ value :: 00:00]
Q.1.36. Immediate Repeat Test Kit 1 Testing Duration (Minutes) [pos :: 35 $$ id :: im_test1_time $$ field_type :: hidden $$ value :: 00:00]
Q.1.37. Immediate Repeat Test Kit 2 Testing Duration (Minutes) [pos :: 36 $$ id :: im_test2_time $$ field_type :: hidden $$ value :: 00:00]

Q.1.38. Outcome Summary [pos :: 37 $$ id :: outcome_summary $$ field_type :: hidden]

Q.1.39. Result Given To Client [pos :: 38 $$ id :: result_given_to_client $$ type :: hidden]

Q.1.40. Take DBS sample [pos :: 39 $$ id :: sample_id $$ condition :: false]

Q.1.41. HIV Testing Summary [pos :: 40 $$ tt_onLoad :: activateNavBtn(); showHIVTestingSummary() $$ optional :: true $$ tt_pageStyleClass :: NoControls NoKeyboard $$ tt_onUnLoad :: window.parent.dashboard.clearMyTimers(); clearTimers("HIV TESTING");]