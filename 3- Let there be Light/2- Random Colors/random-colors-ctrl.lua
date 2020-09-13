
--initilise the color table with 8 diffrent colors 

tableColors= {
    {r = 0 , g = 255, b = 0 } , --green
    {r = 255, g = 255, b = 0 } , --yellow
    {r = 255, g = 69, b = 0 } , --orange
    {r = 255, g = 0, b = 255 } , --megenta
    {r = 51, g = 25, b = 0 } , --brown
    {r = 255, g = 255, b = 255} , --white
    {r = 51, g = 51, b = 255} , --light blue
    {r = 25, g = 0, b = 51} , --purple
    {r = 255, g = 102, b = 102} , --pink
    {r = 0, g = 255, b = 255} --aqua

}


function init()
    --start the step counter
    counter = 0

end

function step()
    counter = counter + 1
    if(robot.id == "fb1") then
        log("fb1 : counter = "..counter)
    end

    if counter % 5 == 1 then
        robotColor = tableColors[robot.random.uniform_int(1 , #tableColors)] --choose a random integer between 1 and the size of the colors table which is 9
                                                                             --then asign the column of that number from the table to the variable
        robot.leds.set_all_colors(robotColor.r,robotColor.g,robotColor.b)   --give the leds of the robot the (r, g, b) values
    end

    
end

function reset()
    init()
   
end

function destroy()
  
end

