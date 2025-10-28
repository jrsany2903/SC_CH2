clear x;
clear y;
incr x 2;
incr y 5;

deffn ADDXY;
    clear z;
    clear xcpy;
    clear ycpy;
    copy xcpy x;
    copy ycpy y;
    while ycpy not 0 do;
        incr z;
        decr ycpy;
    end;
    while xcpy not 0 do;
        incr z;
        decr xcpy;
    end;
    del xcpy;
    del ycpy;
endfn;

deffn LTAB;
    clear acpy;
    clear bcpy;
    clear c;

    copy acpy a;
    copy bcpy b;

    # default: assume a is NOT less than b;
    clear c;

    # loop while both copies are nonzero;
    while acpy not 0 do;
        if bcpy not 0 then;
            decr acpy;
            decr bcpy;
        endif;
        # if bcpy is already 0, break early;
        if bcpy is 0 then;
            # b finished first → a >= b → stop;
            # force exit condition;
            clear acpy;  
        endif;
    end;

    # after loop, check who hit zero first;
    # if acpy is 0 and bcpy not 0 → a < b;
    if acpy is 0 then;
        if bcpy not 0 then;
            # mark as true;
            incr c;   
        endif;
    endif;
    del acpy;
    del bcpy;
endfn;
# padding;
# padding;
ADDXY;
clear result;
copy result z;
clear a;
clear b;
copy a y;
copy b x;
LTAB;
copy result c;


