function weeblyFloat(float_str){
    var int_str = "";
    var decimal_str = "";
    var decimal_place = 1;
    var decimal_found = false;
    for (var i = 0; i < float_str.length; i++){
        var char = float_str[i];
        var parsed_int = parseInt(char);
        if (!isNaN(parsed_int)){
            if (decimal_found === false){
                int_str += parsed_int;
            }
            else{
                decimal_place *= 10;
                decimal_str += parsed_int;
            }
        }
        else if (char.localeCompare(".") === 0){
            if (decimal_found === true){
                break;
            }
            decimal_found = true;
        }
        else{
            break;
        }
    }
    console.log([int_str, decimal_str, decimal_place]);
    if (decimal_found === false || decimal_str.length === 0){
        return parseInt(int_str);
    }
    else{
        if (int_str.length === 0){
            return (parseInt(decimal_str) / decimal_place);
        }
        else{
            return parseInt(int_str) + (parseInt(decimal_str) / decimal_place);
        }
    }
}
    