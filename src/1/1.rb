
def multiple(n)
    arr=[]
    (0..n-1).each do |i|
        if i%3==0 or i%5==0
            arr.append(i)
        end
    end
    # puts(arr)
    return arr.reduce(:+)
    
end

puts(multiple(10))
puts(multiple(1000))