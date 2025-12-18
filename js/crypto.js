function decrypt(data, key) {
  try {
    const decoded = atob(data);
    let out = "";
    for (let i = 0; i < decoded.length; i++) {
      out += String.fromCharCode(
        decoded.charCodeAt(i) ^ key.charCodeAt(i % key.length)
      );
    }
    return out;
  } catch {
    return null;
  }
}
