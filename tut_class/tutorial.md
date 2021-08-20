Method resolution order (MRO)

Start from bottom to top and from left to right
when in MRO we have a super class before subclass then it must be removed from that position in MRO

In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the
class of the object. If it is not found, it is searched in the immediate super class. In the case of multiple super
classes, it is searched left to right, in the order by which was declared by the developer.