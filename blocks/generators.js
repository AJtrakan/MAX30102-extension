
Blockly.Python['MAX30102_SPO2'] = function (block) {
  Blockly.Python.definitions_['impor_MAX30105'] = 'import MAX30105';
  Blockly.Python.definitions_['impor_hrcalc'] = 'import hrcalc';
  Blockly.Python.definitions_['impor_SPo2'] = 'import SPo2';
 
  var code = `SPo2.detect_SPO2()`;
  return [code, Blockly.Python.ORDER_NONE];
};