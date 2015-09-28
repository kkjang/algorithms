"""Thanks for your interest in working at Eventbrite!

As an exercise, please complete the triangle() method below. We've
decided to be helpful and start you off on a good foot: the triangle()
function has a unit test that should pass, in test_triangle(), and
uses a helper called create_triangle_base that is also unit tested.
Once you complete the triangle() function, you should be able to run
this script and instructions will appear.
"""


import itertools


def triangle(input_string):
    """Takes an input string and creates a "triangle".

    A triangle here is defined as a list of lists, where the first
    element is a list with only the first letter from the string,
    the second element is the first two letters from the string,
    etc.

    Uses create_triangle_base to construct a base with the correct length.
    """
    triangle_base = create_triangle_base(input_string)

    # Must make a dereferenced copy of elem so that modifications do not modify the entire base
    for indx, elem in enumerate(triangle_base):
        if indx > 0:
            elem_copy = triangle_base[indx-1][:]
            elem_copy[0] += input_string[indx]
            triangle_base[indx] = elem_copy

    return triangle_base



def test_triangle():
    expected = [
        ['e'],
        ['ev'],
        ['eve'],
        ['even'],
        ['event'],
        ['eventb'],
        ['eventbr'],
        ['eventbri'],
        ['eventbrit'],
        ['eventbrite'],
    ]
    assert(triangle('eventbrite') == expected)


def create_triangle_base(input_string):
    """Takes a string and returns a list of lists.

    This list of lists will have the same length as the input string,
    and the first element in each list will be the first letter of
    the input string.
    """
    # Take the assignment out of the parameter list so c has proper scope
    c = []
    c.append(input_string[0])
    return list(itertools.repeat(c, len(input_string)))


def test_create_triangle_base():
    expected = [
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
        ['e'],
    ]
    assert(create_triangle_base('eventbrite') == expected)


def main():
    print 'Thanks for your interest in working at Eventbrite!'
    print 'If you write your triangle() function correctly, instructions will appear below...'
    test_create_triangle_base()
    try:
        test_triangle()
    except:
        msg = 'Best of luck with the challenge!'
    else:
        # The below should work properly if you complete test_triangle.
        # You really shouldn't have to mess with it / worry about it.
        key = triangle('Eventbrite is awesome!')
        new_ = lambda x, c=__import__('cStringIO').StringIO(): c.writelines(__import__('functools').partial(map, lambda x: next(iter(x)))(x))
        new_(key)
        k = __import__('hashlib').md5(new_.func_defaults[0].getvalue()).hexdigest()
        z = ('i&zD\'w5UITy6w"cLOxM}5WV7P|Yw (H}-YzYx!*DVO*{DvSTa/M&}b[ G7U.z L|.9"L"w5c%V&#0|RNa,'
             'S1ZYL&VyT"-zf ),51x*5)VGy*83EUF7E&*DJ a1Q.+5Y~-/#H3s$Fc_%,)3WVN-Xz%QfxU7C8~~S~9(vPxv5+CJ~zu|XtR1')
        msg = ''.join(chr((ord(a) - ord(b)) % 95 + 32) for a, b, in zip(z, (k*20)[:len(z)]))
    print msg

if __name__ == '__main__':
    main()