package idwall.desafio.string;

public interface StringFormatter {
    /**
     * Should format as described in the challenge
     *
     * @param text to be formatted
     * @return a list of the justified text with each array position containing a line of words
     */
    String format(String text);
}
