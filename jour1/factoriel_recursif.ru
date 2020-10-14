def factoriel(nb_donne)
    if nb_donne <= 1
        return 1
    else
        return nb_donne * factoriel(nb_donne - 1)
    end
end

puts factoriel(3)
