function calc_bmr(height, weight, age , gender){
    if (gender === 'M'){
        return (10 * (weight * 0.453592)) + (6.25 * height) - (5 * age) + 5;
    }
    else {
        return (10 * weight * 0.453592) + (6.25 * height) - (5 * age ) - 161;
    }
}

function maincall(){
    let height = 172.72;
    let weight = 250;
    let gender = "M";
    let age = 28;
    let bmr = calc_bmr(height, weight, gender, age) * 1.20;

    console.log(bmr)
}
maincall()