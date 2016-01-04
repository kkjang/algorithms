// Input is a string
// Parsing is split between the integer portion and the decimal portion of the string
function weeblyFloat(float_str){
    var int_str = "";
    var decimal_str = "";
    var decimal_place = 1;
    var decimal_found = false;
    // Iterate through entire input string
    for (var i = 0; i < float_str.length; i++){
        var char = float_str[i];
        var parsed_int = parseInt(char);
        // If the character can be parsed to an integer
        if (!isNaN(parsed_int)){
            // Continue adding to the int part of the string if no decimal has been found
            if (decimal_found === false){
                int_str += parsed_int;
            }
            // Else increment the decimal place multiple and add to the decimal string
            else{
                decimal_place *= 10;
                decimal_str += parsed_int;
            }
        }
        // Check if the character is a period/decimal point
        else if (char.localeCompare(".") === 0){
            // If a decimal point has already been found, break out of the loop
            if (decimal_found === true){
                break;
            }
            decimal_found = true;
        }
        // If the character is not parsable to an integer and is not a period, break
        else{
            break;
        }
    }
    // If no decimal was found or nothing came after the decimal, just parse the integer portion
    if (decimal_found === false || decimal_str.length === 0){
        return parseInt(int_str);
    }
    else{
        // If there is no integer portion to the string, then just return the decimal
        if (int_str.length === 0){
            return (parseInt(decimal_str) / decimal_place);
        }
        // Else if there is both a decimal and integer portion, return the full float
        else{
            return parseInt(int_str) + (parseInt(decimal_str) / decimal_place);
        }
    }
}
    