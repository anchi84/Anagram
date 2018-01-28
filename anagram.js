function areAnagrams(a, b) {
    return a.toLowerCase().split('').sort().join('').trim() == b.toLowerCase().split('').sort().join('').trim()
}