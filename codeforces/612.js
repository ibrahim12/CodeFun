// var numbers = readline().split(" ").map(function(x){ return parseInt(x); });
// var arr = readline().split(" ").map(function(x){ return parseInt(x); });


// var numbers = [9, 1];
// var arr = [0,1,2,2,2,1,0,1,1];

// var numbers = [8, 1];
// var arr = [0, 1, 0, 1, 0, 1, 0, 1];

// var numbers = [8, 1];
// var arr = [0, 0, 0 ,0, 0, 0, 0, 0];

// var numbers =[8, 1];
// var arr =  [1, 2, 3, 4, 5, 6, 7, 8];

// var numbers =[20, 7];
// var arr =  [1, 2, 3, 4, 5, 6, 7, 8];
var numbers = [20, 7];
var arr = [0,6,0,0,0,-7,-8,9,-7,4,7,2,-4,4,-5,2,6,8,-2,-7];



var MAXI = arr.length+1;

var n = numbers[0];

var grid = new Array(n);

var cd, ccd;

for(var i = 1; i <= n; i++){
    grid[i] = new Array(n);
    for(var j=1; j<= n; j++){
        
        cd = j - i;
        ccd = i - j;

        if( cd > n) cd -= n;
        if( cd < 0) cd += n;   

        if( ccd > n) ccd -= n;
        if( ccd < 0) ccd += n;
        
        grid[i][j] = Math.abs(cd) < Math.abs(ccd) ? cd : -ccd;
        
        // print(i, j, cd, ccd, grid[i][j]);
    }
}

// for(var i = 0; i < n; i++){
//     print(grid[i]);
// }


var s  = numbers[1];

var iarr = [];
for(var index = 0; index < arr.length; index++){
   iarr.push(index);
}

var sorted = iarr.sort(function(a, b){ return arr[a] < arr[b] ? -1 : arr[a] > arr[b] ? 1 : 0 });
print(sorted);
var groups = [];


var groupIndex = 0;

for(var index = 0 ;index < sorted.length; index ++){
    var sindex = sorted[index];
    var valueToPush = arr[sindex];
    
    if( groups.length === 0 ){
        
        groups.push([sindex+1]);
        oldValueToPush = valueToPush;

    }
    else{

        if( valueToPush != oldValueToPush ){
           groupIndex++;
           groups[groupIndex] = [];
           oldValueToPush = valueToPush;
        }
        
        groups[groupIndex].push(sindex+1);
    }
}

for(index = 0; index < groups.length; index++){
    print(index + ': ', groups[index]);
}


print('-');


total = 0;
var costlist = [];

function findDirection1(start, group){
    // print(start);
    // print(group);


    var cost, nextsi, value, index, len, ccost, cindex, mark=true;

    nextsi = start;
    cost = MAXI;

    while(group.length !== 0 && mark){
        mark = false;
        cost = MAXI;

        for(index = 0, len = group.length; index < len; index++ ){
            value = group[index];
            if( value < 0)continue;
            mark = true;

            if( cost > Math.abs(grid[nextsi][value])){
                cost = Math.abs(grid[nextsi][value]);
                ccost = grid[nextsi][value];
                cindex = index;
            }
        }

        if(!mark)break;

        costlist.push(ccost);

        total += Math.abs(ccost);
        nextsi = group[cindex];
        group[cindex] = -1;

        // print('nextsi', nextsi);

    }

    return nextsi;

}




start = s;
for(var index = 0; index < groups.length; index++){
    start = findDirection1(start, groups[index]);
    // print('s', start);
    // break;

}
print(total);
for(var index = 0, len = costlist.length; index < len; index++){
    if( costlist[index] >= 0){
        print('+' + costlist[index]);
    }else{
        print(costlist[index]);
    }
}


